from fastapi import APIRouter, Request, status
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/nutricionista")

templates = Jinja2Templates(directory="templates")

@router.get("/")  
def get_root(request: Request):
    return templates.TemplateResponse("pages/nutricionista/pagina_inicial_nutricionista.html", status.HTTP_303_SEE_OTHER)

@router.get("/inicial")  
def get_root(request: Request):
    return templates.TemplateResponse("pages/nutricionista/pagina_inicial_nutricionista.html", {"request": request})

@router.get("/configuracoes")  
async def get_configuracoes(request: Request):
    return templates.TemplateResponse("pages/nutricionista/configuracoes_nutricionista.html", {"request": request})

@router.get("/sobre")  
async def get_sobre(request: Request):
    return templates.TemplateResponse("pages/nutricionista/sobre_nutricionista.html", {"request": request})

@router.get("/termos")  
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/nutricionista/termos_nutricionista.html", {"request": request})

@router.get("/contato")  
async def get_contato(request: Request):
    return templates.TemplateResponse("pages/nutricionista/contato_nutri.html", {"request": request})

@router.get("/suporte")  
async def get_suporte(request: Request):
    return templates.TemplateResponse("pages/nutricionista/suporte_nutricionista.html", {"request": request})

@router.get("/politicadeprivacidade")  
async def get_politicadeprivacidade(request: Request):
    return templates.TemplateResponse("pages/nutricionista/politicadeprivacidade_nutricionista.html", {"request": request})

@router.get("/planos")  
async def get_planos(request: Request):
    return templates.TemplateResponse("pages/nutricionista/plano_nutricionista.html", {"request": request})

@router.get("/artigos")  
async def get_artigos(request: Request):
    return templates.TemplateResponse("pages/nutricionista/artigos_nutricionista.html", {"request": request})

@router.get("/dietas_postadas")  
async def get_dietas_postadas(request: Request):
    return templates.TemplateResponse("pages/nutricionista/dietas_postadas_nutricionista.html", {"request": request})

@router.get("/receitas_postadas")  
async def get_receitas_postadas(request: Request):
    return templates.TemplateResponse("pages/nutricionista/receitas_postadas_nutricionista.html", {"request": request})

@router.get("/artigos_postados")  
async def get_artigos_postados(request: Request):
    return templates.TemplateResponse("pages/personal/artigos_postados_nutricionista.html", {"request": request})