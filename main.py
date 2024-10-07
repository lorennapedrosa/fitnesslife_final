import dotenv
from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from repositories.usuario_repo import UsuarioRepo
from routes.anonimo_routes import router as main_router
from routes.usuario_routes import router as usuario_router
from routes.personal_routes import router as personal_router
from routes.cliente_routes import router as cliente_router
from routes.nutricionista_routes import router as nutricionista_router
from util.auth import checar_autenticacao, checar_autorizacao

UsuarioRepo.criar_tabela()
dotenv.load_dotenv()
app = FastAPI(dependencies=[Depends(checar_autorizacao)])
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware("http")(checar_autenticacao)
app.include_router(main_router)
app.include_router(usuario_router)
app.include_router(cliente_router)
app.include_router(personal_router)
app.include_router(nutricionista_router)