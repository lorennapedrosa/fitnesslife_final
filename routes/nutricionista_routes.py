from fastapi import APIRouter, Request, status
from fastapi.templating import Jinja2Templates

def common_view_params(request: Request, show_header=True, show_footer=True, show_sidebar=True):
    return {
        "request": request,
        "show_header": show_header,
        "show_footer": show_footer,
        "show_sidebar": show_sidebar
    }
#
# NUTRICIONISTA
#
router = APIRouter(prefix="/nutricionista")

templates = Jinja2Templates(directory="templates")

@router.get("/index")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/nutricionista/index.html", {"request": request})

@router.get("/configuracoes_nutricionista")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/nutricionista/configuracoes_nutricionista.html", {"request": request})

@router.get("/sobre_nutricionista")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/nutricionista/sobre_nutricionista.html", {"request": request})

@router.get("/termos_nutricionista")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/nutricionista/termos_nutricionista.html", {"request": request})

@router.get("/contato_nutricionista")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/nutricionista/contato_nutri.html", {"request": request})

@router.get("/suporte_nutricionista")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/nutricionista/suporte_nutricionista.html", {"request": request})

@router.get("/politicadeprivacidade_nutricionista")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/nutricionista/politicadeprivacidade_nutricionista.html", {"request": request})

@router.get("/planos_nutricionista")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/nutricionista/plano_nutricionista.html", {"request": request})

@router.get("/artigos_nutricionista")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/nutricionista/artigos_nutricionista.html", {"request": request})

