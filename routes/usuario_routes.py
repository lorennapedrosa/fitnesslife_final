from datetime import date
from fastapi import APIRouter, Form, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models.usuario_model import Usuario
from repositories.usuario_repo import UsuarioRepo
from util.auth import conferir_senha, obter_hash_senha

'''def common_view_params(request: Request, show_header=True, show_footer=True, show_sidebar=True):
    return {
        "request": request,
        "show_header": show_header,
        "show_footer": show_footer,
        "show_sidebar": show_sidebar
    }'''

router = APIRouter(prefix="/usuario")

templates = Jinja2Templates(directory="templates")

@router.get("/tema")
async def get_tema(request: Request):
    temas = ["default", "cerulean", "cosmo", "cyborg", "darkly", "flatly", "journal", "litera", "lumen", "lux", "materia", "minty", "morph", "pulse", "quartz", "sandstone", "simplex", "sketchy", "slate", "solar", "spacelab", "superhero", "united", "vapor", "yeti", "zephyr"]
    return templates.TemplateResponse("pages/usuario/tema.html", {"request": request, "temas": temas})

@router.post("/post_tema")
async def post_tema(tema: str = Form(...)):
    response = RedirectResponse("/usuario/tema", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(
        key="tema",
        value=tema,
        max_age=3600*24*365*10,
        httponly=True,
        samesite="lax"
    )
    return response

@router.get("/recuperar_senha")
async def get_recuperar_senha(request: Request):
    return templates.TemplateResponse("pages/usuario/esqueceu_sua_senha.html")



@router.get("/redefinir_senha")
async def get_dados(request: Request):    
    return templates.TemplateResponse("pages/usuario/redefinir_senha.html", {"request": request})

@router.post("/post_senha")
async def post_senha(
    request: Request, 
    senha_atual: str = Form(...),    
    nova_senha: str = Form(...),
    conf_nova_senha: str = Form(...)):
    id_usuario = request.state.usuario.id
    usuario = UsuarioRepo.obter_por_id(id_usuario)    
    if nova_senha == conf_nova_senha and conferir_senha(senha_atual, usuario.senha):
        UsuarioRepo.atualizar_senha(id_usuario, nova_senha)
    return RedirectResponse("pages/usuario/refinir_senha", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/dados")
async def get_dados(request: Request):
    id_usuario = request.state.usuario.id
    usuario = UsuarioRepo.obter_por_id(id_usuario)
    return templates.TemplateResponse("pages/usuario/dados.html", {"request": request, "usuario": usuario})
