from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from util.auth import NOME_COOKIE_AUTH

router = APIRouter(prefix="/usuario")

templates = Jinja2Templates(directory="templates")

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
