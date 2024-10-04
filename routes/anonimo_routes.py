from datetime import time
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models.usuario_model import Usuario
from repositories.usuario_repo import UsuarioRepo
from util.auth import NOME_COOKIE_AUTH, criar_token, obter_hash_senha

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/")
async def get_root(request: Request):
    usuario = request.state.usuario if hasattr(request.state, "usuario") else None
    if usuario:   
        if usuario.perfil == 1:
            return RedirectResponse("/cliente", status_code=status.HTTP_303_SEE_OTHER)
        if usuario.perfil == 2:
            return RedirectResponse("/nutricionista", status_code=status.HTTP_303_SEE_OTHER)
        if usuario.perfil == 3:
            return RedirectResponse("/personal", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("pages/anonimo/index.html", {"request": request})
    

@router.get("/login")
async def get_login(request: Request):
    return templates.TemplateResponse("pages/anonimo/login.html", {"request": request})


@router.post("/post_login")
async def post_entrar(
    email: str = Form(...), 
    senha: str = Form(...)):
    usuario = UsuarioRepo.checar_credenciais(email, senha)
    if usuario is None:
        response = RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)
        return response
    token = criar_token(usuario.id, usuario.nome, usuario.email, usuario.perfil)
    nome_perfil = None
    match (usuario.perfil):
        case 1: nome_perfil = "cliente"
        case 2: nome_perfil = "nutricionista"
        case 3: nome_perfil = "educador físico"
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
async def get_cadastrar(request: Request):
    return templates.TemplateResponse("pages/anonimo/inscrever.html", {"request": request})


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
    usuario = Usuario(
        nome=nome,
        email=email,
        senha=senha_hash,
        perfil=perfil)
    UsuarioRepo.inserir(usuario)
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/recuperar_senha")
async def get_recuperar_senha(request: Request):
    return templates.TemplateResponse("pages/anonimo/esqueceu_sua_senha.html")
