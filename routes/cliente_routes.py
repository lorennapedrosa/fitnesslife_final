import calendar
from datetime import date, datetime
from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/cliente")


templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/perfil.html", {"request": request})

@router.get("/perfil")
async def get_perfil(request: Request):
    return templates.TemplateResponse("pages/cliente/perfil.html", {"request": request})


@router.get("/planos")
async def get_planos(request: Request):
    return templates.TemplateResponse("pages/cliente/planos.html", {"request": request})

@router.get("/suporte")
async def get_suporte(request: Request):
    return templates.TemplateResponse("pages/cliente/suporte.html", {"request": request})

@router.get("/termos")
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/cliente/termos.html", {"request": request})

@router.get("/politicadeprivacidade")
async def get_politicadeprivacidade(request: Request):
    return templates.TemplateResponse("pages/cliente/politicadeprivacidade.html", {"request": request})

@router.get("/painelcliente")
async def get_painelcliente(request: Request):
    return templates.TemplateResponse("pages/cliente/painelcliente.html", {"request": request})


@router.get("/calendario")
async def get_painelcliente(request: Request):
    return templates.TemplateResponse("pages/cliente/calendario.html", {"request": request})

@router.get("/exercicios")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/exercicios.html", {"request": request})

@router.get("/artigos")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/artigos.html", {"request": request})

@router.get("/configuracoes")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/configuracoes.html", {"request": request})

@router.get("/contato")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/contato.html", {"request": request})

@router.get("/sobre")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/sobre.html", {"request": request})

@router.get("/professores")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/professores.html", {"request": request})

@router.get("/perguntasfrequentes")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/perguntasfrequentes.html", {"request": request})

@router.get("/mensagens")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/mensagens.html", {"request": request})

@router.get("/estatisticas")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/estatisticas.html", {"request": request})

@router.get("/receitas")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/receitas.html", {"request": request})

@router.get("/rotina")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/rotina.html", {"request": request})

@router.get("/explorarrotina")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/explorar_rotina.html", {"request": request})

@router.get("/treinamentovazio")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/treinamento_vazio.html", {"request": request})

@router.get("/alimentacao")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/alimentacao.html", {"request": request})