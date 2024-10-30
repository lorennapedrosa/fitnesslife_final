from datetime import datetime, timedelta
import os
from typing import Optional
from fastapi import HTTPException, Request
from fastapi.responses import RedirectResponse
import jwt
from dto.usuario_autenticado_dto import UsuarioAutenticadoDto

NOME_COOKIE_AUTH = "jwt-token"

def criar_token_jwt(usuarioAutenticadoDto: UsuarioAutenticadoDto) -> str:
    dados_token = {
        "id": usuarioAutenticadoDto.id,
        "nome": usuarioAutenticadoDto.nome,
        "data_nascimento": usuarioAutenticadoDto.data_nascimento,
        "email": usuarioAutenticadoDto.email,
        "perfil": usuarioAutenticadoDto.perfil,
        "exp": datetime.now() + timedelta(days=1),
    }
    secret_key = os.getenv("JWT_TOKEN_SECRET_KEY")
    algorithm = os.getenv("JWT_TOKEN_ALGORITHM")
    return jwt.encode(dados_token, secret_key, algorithm)


def decodificar_token_jwt(token: str) -> Optional[UsuarioAutenticadoDto]:
    secret_key = os.getenv("JWT_TOKEN_SECRET_KEY")
    algorithm = os.getenv("JWT_TOKEN_ALGORITHM")
    try:
        dados_token = jwt.decode(token, secret_key, algorithm)
        return UsuarioAutenticadoDto(
            id=int(dados_token["id"]),
            nome=dados_token["nome"],
            data_nascimento=dados_token["data_nascimento"],
            email=dados_token["email"],
            perfil=int(dados_token["perfil"])
        )
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def adicionar_token_jwt(response: RedirectResponse, token: str, dias: int = 1):
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=3600*24*dias,
        httponly=True,
        samesite="lax"
    )


def remover_token_jwt(response: RedirectResponse):
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value="",
        max_age=0,
        httponly=True,
        samesite="lax",
    )

async def checar_autenticacao(request: Request, call_next):
    token = request.cookies.get(NOME_COOKIE_AUTH, None)
    if token:
        usuario_autenticado_dto = decodificar_token_jwt(token)
        request.state.usuario = usuario_autenticado_dto
    response = await call_next(request)
    return response


async def checar_autorizacao(request: Request):
    usuario = request.state.usuario if hasattr(request.state, "usuario") else None
    area_do_cliente = request.url.path.startswith("/cliente")
    area_do_nutricionista = request.url.path.startswith("/nutricionista")
    area_do_personal = request.url.path.startswith("/personal")
    if (area_do_cliente or area_do_nutricionista or area_do_personal) and usuario is None:
        raise HTTPException(status_code=401, detail="Usuário não autenticado!")
    if area_do_cliente and usuario.perfil != 1:
        raise HTTPException(status_code=403, detail="Usuário não autorizado!")
    if area_do_nutricionista and usuario.perfil != 2:
        raise HTTPException(status_code=403, detail="Usuário não autorizado!")
    if area_do_personal and usuario.perfil != 3:
        raise HTTPException(status_code=403, detail="Usuário não autorizado!")