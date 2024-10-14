from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models.usuario_model import Usuario
from repositories.usuario_repo import UsuarioRepo
from util.auth import NOME_COOKIE_AUTH, criar_token, obter_hash_senha


router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_root(request: Request):
    usuario = request.state.usuario if hasattr(request.state, "usuario") else None
    if not usuario or not usuario.email:
        return RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)        
    if usuario.perfil == 1:
        return RedirectResponse("/cliente", status_code=status.HTTP_303_SEE_OTHER)
    if usuario.perfil == 2:
        return RedirectResponse("/nutricionista", status_code=status.HTTP_303_SEE_OTHER) 
    if usuario.perfil == 3:
        return RedirectResponse("/personal", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/login")
async def get_login(request: Request):
    return templates.TemplateResponse("pages/anonimo/login.html", {"request": request})

@router.post("/post_login")
async def post_login(
    email: str = Form(...), 
    senha: str = Form(...)):
    usuario = UsuarioRepo.checar_credenciais(email, senha)
    if usuario is None:
        response = RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
        return response
    token = criar_token(usuario[0], usuario[1], usuario[2], usuario[3])
    nome_perfil = None
    match (usuario[3]):
        case 1: nome_perfil = "cliente"
        case 2: nome_perfil = "nutricionista"
        case 3: nome_perfil = "personal"
        case _: nome_perfil = ""
    
    response = RedirectResponse(f"/{nome_perfil}", status_code=status.HTTP_303_SEE_OTHER)    
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=3600*24*365*10,
        httponly=True,
        samesite="lax"
    )
    return response

@router.get("/inscrever")
async def get_inscrever(request: Request):
    options_perfis = [
        {'value' : '1', 'label': 'Cliente' },
        {'value' : '2', 'label': 'Nutricionista' },
        {'value' : '3', 'label' : 'Personal'}
    ]
    return templates.TemplateResponse("pages/anonimo/inscrever.html", {"request": request, "options_perfis": options_perfis})

@router.post("/post_inscrever")
async def post_inscrever(
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    confsenha: str = Form(...),
    perfil: int = Form(...)):
    if senha != confsenha:
        return RedirectResponse("/inscrever", status_code=status.HTTP_303_SEE_OTHER)
    senha_hash = obter_hash_senha(senha)
    usuario = Usuario(None, nome, email, senha_hash, perfil)
    UsuarioRepo.inserir(usuario)
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/sair")
async def get_sair():
    response = RedirectResponse("/", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value="",
        max_age=1,
        httponly=True,
        samesite="lax")
    return response    