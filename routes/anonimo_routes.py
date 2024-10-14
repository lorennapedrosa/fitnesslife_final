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
    
    # Se não houver usuário ou se o email estiver ausente, redireciona para a página de login
    if not usuario or not usuario.email:
        return templates.TemplateResponse("pages/anonimo/index.html", {"request": request})
    
    # Usuário autenticado, redireciona para a página correspondente ao perfil
    match usuario.perfil:
        case 1:
            return RedirectResponse("/cliente", status_code=status.HTTP_303_SEE_OTHER)
        case 2:
            return RedirectResponse("/nutricionista", status_code=status.HTTP_303_SEE_OTHER)
        case 3:
            return RedirectResponse("/personal", status_code=status.HTTP_303_SEE_OTHER)
        case _:
            return RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)

    
@router.get("/login")
async def get_login(request: Request):
    return templates.TemplateResponse("pages/anonimo/login.html", {"request": request})

@router.post("/post_login")
async def post_login(
    email: str = Form(...), 
    senha: str = Form(...)):
    usuario = UsuarioRepo.checar_credenciais(email, senha)
    if usuario is None:
        response = RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)
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
    return templates.TemplateResponse("pages/anonimo/inscrever.html", {"request": request})

@router.post("/post_inscrever")
async def post_inscrever(
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    confsenha: str = Form(...),
    perfil: int = Form(...)):
    
    # Verifica se as senhas correspondem
    if senha != confsenha:
        return RedirectResponse("/inscrever", status_code=status.HTTP_303_SEE_OTHER)
    
    # Verifica se o perfil é válido
    if perfil not in [1, 2, 3]:
        return RedirectResponse("/inscrever", status_code=status.HTTP_400_BAD_REQUEST)

    # Verifica se o email já está cadastrado
    usuario_existente = UsuarioRepo.buscar_por_email(email)
    if usuario_existente:
        return RedirectResponse("/inscrever", status_code=status.HTTP_409_CONFLICT)
    
    # Cria o hash da senha
    senha_hash = obter_hash_senha(senha)

    # Cria o objeto usuário e insere no banco de dados
    usuario = Usuario(
        nome=nome,
        email=email,
        senha=senha_hash,
        perfil=perfil
    )
    try:
        UsuarioRepo.inserir(usuario)
    except Exception as e:
        print(f"Erro ao inserir usuário: {e}")
        return RedirectResponse("/inscrever", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Redireciona para a página de login
    return RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/recuperar_senha")
async def get_recuperar_senha(request: Request):
    return templates.TemplateResponse("pages/anonimo/esqueceu_sua_senha.html", {"request": request})




