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
# PERSONAL
#

router = APIRouter(prefix="/personal")

templates = Jinja2Templates(directory="templates")

@router.get("/personal_inicial")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/personal/index.html", {"request": request})

@router.get("/configuracoes_personal")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/personal/configuracoes_personal.html", {"request": request})

@router.get("/sobre_personal")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/personal/sobre_personal.html", {"request": request})

@router.get("/termos_personal")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/personal/termos_personal.html", {"request": request})

@router.get("/contato_personal")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/personal/contato_personal.html", {"request": request})

@router.get("/suporte_personal")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/personal/suporte_personal.html", {"request": request})

@router.get("/politicadeprivacidade_personal")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/personal/politicadeprivacidade_personal.html", {"request": request})

@router.get("/planos_personal")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/personal/plano_personal.html", {"request": request})

@router.get("/artigos_personal")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/personal/artigos_personal.html", {"request": request})

@router.get("/adicionar_exercicio_personal")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/personal/adicionar_exercicio_personal.html", {"request": request})

@router.get("/adicionar_ficha_personal")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/personal/adicionar_ficha_personal.html", {"request": request})

@router.get("/historico_alunos_personal")  
def get_root(request: Request):

    return templates.TemplateResponse("pages/personal/historico_alunos_personal.html", {"request": request})
