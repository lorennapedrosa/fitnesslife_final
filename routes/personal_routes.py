from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/personal")

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/personal/pagina_inicial_personal.html", {"request": request})

@router.get("/inicial")  
async def get_inicial(request: Request):
    return templates.TemplateResponse("pages/personal/pagina_inicial_personal.html", {"request": request})

@router.get("/configuracoes")  
async def get_configuracoes(request: Request):
    return templates.TemplateResponse("pages/personal/configuracoes_personal.html", {"request": request})

@router.get("/sobre")  
async def get_sobre(request: Request):
    return templates.TemplateResponse("pages/personal/sobre_personal.html", {"request": request})

@router.get("/termos")  
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/personal/termos_personal.html", {"request": request})

@router.get("/contato")  
async def contato(request: Request):
    return templates.TemplateResponse("pages/personal/contato_personal.html", {"request": request})

@router.get("/suporte")  
async def get_suporte(request: Request):
    return templates.TemplateResponse("pages/personal/suporte_personal.html", {"request": request})

@router.get("/politicadeprivacidade")  
async def get_politicadeprivacidade(request: Request):
    return templates.TemplateResponse("pages/personal/politicadeprivacidade_personal.html", {"request": request})

@router.get("/planos")  
async def get_planos(request: Request):
    return templates.TemplateResponse("pages/personal/plano_personal.html", {"request": request})

@router.get("/artigos")  
async def get_artigos(request: Request):
    return templates.TemplateResponse("pages/personal/artigos_personal.html", {"request": request})

@router.get("/adicionar_exercicio")  
async def get_adicionar_exercicio(request: Request):
    return templates.TemplateResponse("pages/personal/adicionar_exercicio_personal.html", {"request": request})

@router.get("/adicionar_ficha")  
async def get_adicionar_ficha(request: Request):
    return templates.TemplateResponse("pages/personal/adicionar_ficha_personal.html", {"request": request})

@router.get("/historico_alunos")  
async def get_historico_alunos(request: Request):
    return templates.TemplateResponse("pages/personal/historico_alunos_personal.html", {"request": request})

@router.get("/meusalunos")  
async def get_meusalunos(request: Request):
    return templates.TemplateResponse("pages/personal/meus_alunos_personal.html", {"request": request})

@router.get("/artigos_postados")  
async def get_artigos_postados(request: Request):
    return templates.TemplateResponse("pages/personal/artigos_postados_personal.html", {"request": request})

@router.get("/exercicios_postados")  
async def get_exercicios_postados(request: Request):
    return templates.TemplateResponse("pages/personal/exercicios_postados_personal.html", {"request": request})

@router.get("/fichas_postadas")  
async def get_fichas_postadas(request: Request):
    return templates.TemplateResponse("pages/personal/fichas_postadas_personal.html", {"request": request})
