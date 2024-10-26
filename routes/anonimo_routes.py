from datetime import datetime, timedelta
import bcrypt
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models.usuario_model import Usuario
from repositories.usuario_repo import UsuarioRepo
from util.auth import NOME_COOKIE_AUTH, criar_token_jwt
from util.mensagens import adicionar_mensagem_erro, adicionar_mensagem_sucesso
from util.validators import *


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/")
async def get_root(request: Request):
    usuario = request.state.usuario if hasattr(request.state, "usuario") else None
    if not usuario or not usuario.email:
        return templates.TemplateResponse(
            "pages/anonimo/index.html", {"request": request}
        )
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
async def post_login(email: str = Form(...), senha: str = Form(...)):
    usuario = UsuarioRepo.checar_credenciais(email, senha)
    if usuario is None:
        print(f"Login falhou para o email: {email}")
        response = RedirectResponse(
            "/login?erro=credenciais_invalidas", status_code=status.HTTP_303_SEE_OTHER
        )
        return response
    token = criar_token_jwt(usuario[0], usuario[1], usuario[2], usuario[3])
    nome_perfil = None
    match (usuario[3]):
        case 1:
            nome_perfil = "cliente"
        case 2:
            nome_perfil = "nutricionista"
        case 3:
            nome_perfil = "personal"
        case _:
            nome_perfil = ""
    response = RedirectResponse(
        f"/{nome_perfil}", status_code=status.HTTP_303_SEE_OTHER
    )
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=3600 * 24 * 365 * 10,  # Token com validade longa
        httponly=True,
        samesite="lax",
    )
    print(f"Login bem-sucedido para o email: {email}")
    return response


@router.get("/inscrever")
async def get_inscrever(request: Request):
    options_perfis = [
        {"value": "1", "label": "Cliente"},
        {"value": "2", "label": "Nutricionista"},
        {"value": "3", "label": "Personal"},
    ]
    return templates.TemplateResponse(
        "pages/anonimo/inscrever.html",
        {"request": request, "options_perfis": options_perfis},
    )


@router.post("/post_inscrever")
async def post_inscrever(request: Request):
    # capturar os dados do formulário de cadastro como um dicionário
    dados = dict(await request.form())
    # normalizar os dados para tipificar os valores corretamente
    dados["perfil"] = int(dados["perfil"])
    # validar dados do formulário
    erros = {}
    # validação da senha igual à confirmação da senha
    if is_matching_fields(
        dados["senha"],
        "senha",
        "Senha",
        dados["confsenha"],
        "Confirmação de Senha",
        erros,
    ):
        dados.pop("confsenha")
    # validação do nome
    is_person_fullname(dados["nome"], "nome", "Nome", erros)
    is_size_between(dados["nome"], "nome", "Nome", 5, 64, erros)
    # validação do email
    is_email(dados["email"], "email", "E-mail", erros)
    # validação da senha
    is_password(dados["senha"], "senha", "Senha", erros)
    # se tiver erros, monta a exibição dos erros e reexibe a página de inscrição
    if erros:
        response = templates.TemplateResponse(
            "pages/anonimo/inscrever.html",
            {"request": request, "dados": dados, "erros": erros},
        )
        adicionar_mensagem_erro(
            response, "Há erros no formulário. Corrija-os e tente novamente."
        )
        return response
    # se não tiver erros, criptografa a senha com bcrypt
    senha_hash = bcrypt.hashpw(dados["senha"].encode(), bcrypt.gensalt())
    dados["senha"] = senha_hash.decode()
    # TODO: adicionar campos de formulario para data de nascimento e remover a linha a seguir
    dados["data_nascimento"] = datetime.now() - timedelta(days=365 * 18)
    # criar um objeto Usuario com os dados do dicionário
    usuario = Usuario(**dados)
    # inserir o objeto Usuario no banco de dados usando o repositório
    usuario = UsuarioRepo.inserir(usuario)
    # se inseriu com sucesso, redirecionar para a página de login
    if usuario:
        response = RedirectResponse("/login", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_sucesso(response, "Cadastro realizado com sucesso!")
        return response
    # se não inseriu, redirecionar para a página de cadastro com mensagem de erro
    else:
        response = RedirectResponse("/inscrever", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(
            response,
            "Ocorreu um problema ao realizar seu cadastro. Tente novamente mais tarde.",
        )
        return response


@router.get("/sair")
async def get_sair():
    response = RedirectResponse("/", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
    response.set_cookie(
        key=NOME_COOKIE_AUTH, value="", max_age=1, httponly=True, samesite="lax"
    )
    return response


@router.get("/esqueceu_sua_senha")
async def get_login(request: Request):
    return templates.TemplateResponse(
        "pages/anonimo/esqueceu_sua_senha.html", {"request": request}
    )


@router.get("/redefinir_senha")
async def get_login(request: Request):
    return templates.TemplateResponse(
        "pages/anonimo/redefinir_senha.html", {"request": request}
    )
