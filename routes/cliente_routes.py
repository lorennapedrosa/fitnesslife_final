import calendar
from datetime import datetime
from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/cliente")


templates = Jinja2Templates(directory="templates")

@router.get("/planos")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/planos.html", {"request": request})

@router.get("/suporte")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/suporte.html", {"request": request})

@router.get("/termos")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/termos.html", {"request": request})

@router.get("/politicadeprivacidade")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/politicadeprivacidade.html", {"request": request})

@router.get("/painelcliente")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/painelcliente.html", {"request": request})

@router.get("/perfil")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/perfil.html", {"request": request})

@router.get("/calendario/{year?}/{month?}", response_class=HTMLResponse)
def get_calendario(request: Request, year: int = None, month: int = None):
    try:
        today = datetime.date.today()
        if not year: year = today.year
        if not month: month = today.month
        cal = calendar.Calendar()
        month_days = cal.monthdayscalendar(year, month)
        view_model = {
            "request": request,
            "year": year,
            "month": month,
            "month_days": month_days,
            "calendar": calendar,
        }        
        return templates.TemplateResponse("pages/cliente/calendario.html", view_model)
    except calendar.IllegalMonthError:
        raise HTTPException(status_code=400, detail="Mes deve estar entre 1 e 12")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/dia/{date}", response_class=HTMLResponse)
async def read_dia(request: Request, date: str):    
    return templates.TemplateResponse("pages/cliente/dia_detalhe.html", {"request": request})

@router.get("/alimentacao", response_class=HTMLResponse)
async def get_alimentacao(request: Request, day: str = None):
    today = datetime.date.today().isoformat()
    if not day:
        day = today
    view_model = {
        "request": request,
        "day": day,
        "alimentacao": []
    }
    return templates.TemplateResponse("pages/cliente/alimentacao.html", view_model)

@router.get("/exercicios")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/exercicios.html", {"request": request})

@router.get("/artigos")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/artigos.html", {"request": request})

@router.get("/configuracoes")
def get_root(request: Request):
    return templates.TemplateResponse("configuracoes.html", {"request": request})

@router.get("/contato")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/contato.html", {"request": request})

@router.get("/sobre")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/sobre.html", {"request": request})

@router.get("/professores")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/professores.html", {"request": request})

@router.get("/perguntasfrequentes")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/perguntasfrequentes.html", {"request": request})

@router.get("/mensagens")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/mensagens.html", {"request": request})

@router.get("/estatisticas")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/estatisticas.html", {"request": request})

@router.get("/receitas")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/receitas.html", {"request": request})

@router.get("/rotina")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/rotina.html", {"request": request})

@router.get("/explorarrotina")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/explorar_rotina.html", {"request": request})

@router.get("/treinamentovazio")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/treinamento_vazio.html", {"request": request})

@router.get("/perguntasfrequentes")
def get_root(request: Request):
    return templates.TemplateResponse("pages/cliente/perguntasfrequentes.html", {"request": request})