import calendar
from datetime import datetime
from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

#
# CLIENTE
#

def common_view_params(request: Request, show_header=True, show_footer=True, show_sidebar=True):
    return {
        "request": request,
        "show_header": show_header,
        "show_footer": show_footer,
        "show_sidebar": show_sidebar
    }

router = APIRouter(prefix="/cliente")


templates = Jinja2Templates(directory="templates")

@router.get("/planos")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/planos.html", common_view_params(request))

@router.get("/suporte")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/suporte.html", common_view_params(request))

@router.get("/termos")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/termos.html", common_view_params(request))

@router.get("/politicadeprivacidade")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/politicadeprivacidade.html", common_view_params(request))

@router.get("/painelcliente")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/painelcliente.html", common_view_params(request))

@router.get("/perfil")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/perfil.html", common_view_params(request))

@router.get("/calendario", response_class=HTMLResponse)
async def read_calendario_current(request: Request):
    today = datetime.date.today()
    year = today.year
    month = today.month
    return RedirectResponse(url=f"/pages/cliente/calendario/{year}/{month}")

@router.get("/calendario/{year}/{month}", response_class=HTMLResponse)
async def read_calendario(request: Request, year: int, month: int):
    try:
        cal = calendar.Calendar()
        month_days = cal.monthdayscalendar(year, month)
        view_model = {
            "request": request,
            "year": year,
            "month": month,
            "month_days": month_days,
            "calendar": calendar,
        }
        return templates.TemplateResponse("pages/cliente/calendario.html", common_view_params(request))
    except calendar.IllegalMonthError:
        raise HTTPException(status_code=400, detail="Month must be in 1..12")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/dia/{date}", response_class=HTMLResponse)
async def read_dia(request: Request, date: str):
    details = registros.get(date, {"exercises": [], "meals": []})
    view_model = {
        "request": request,
        "date": date,
        "details": details
    }
    return templates.TemplateResponse("pages/cliente/dia_detalhe.html", common_view_params(request))

@router.get("/alimentacao", response_class=HTMLResponse)
async def get_alimentacao(request: Request, day: str = None):
    today = datetime.date.today().isoformat()
    if not day:
        day = today
    
    view_model = {
        "request": request,
        "day": day,
        **alimentacao.get(day, {})
    }
    return templates.TemplateResponse("pages/cliente/alimentacao.html", common_view_params(request))

@router.get("/api/alimentacao", response_class=JSONResponse)
async def get_alimentacao_api(day: str = None):
    today = datetime.date.today().isoformat()
    if not day:
        day = today
    return alimentacao.get(day, {})

@router.get("/exercicios")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/exercicios.html", common_view_params(request))

@router.get("/artigos")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/artigos.html", common_view_params(request))

@router.get("/configuracoes")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("configuracoes.html", common_view_params(request))

@router.get("/contato")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/contato.html", common_view_params(request))

@router.get("/sobre")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/sobre.html", common_view_params(request))

@router.get("/professores")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/professores.html", common_view_params(request))

@router.get("/perguntasfrequentes")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/perguntasfrequentes.html", common_view_params(request))

@router.get("/mensagens")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/mensagens.html", common_view_params(request))

@router.get("/estatisticas")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/estatisticas.html", common_view_params(request))

@router.get("/receitas")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/receitas.html", common_view_params(request))


@router.get("/rotina")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/rotina.html", common_view_params(request))

@router.get("/explorarrotina")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/explorar_rotina.html", common_view_params(request))

@router.get("/treinamentovazio")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/treinamento_vazio.html", common_view_params(request))

@router.get("/perguntasfrequentes")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("pages/cliente/perguntasfrequentes.html", common_view_params(request))

user_data = {
    "email": "usuario@exemplo.com",
    "senha": "senha_antiga",
    "codigo_verificacao": "123456"
}

registros = {
    "2024-06-27": {
        "exercises": ["Corrida - 5km", "Abdominais - 3 séries de 20"],
        "meals": ["Café da manhã: Aveia com frutas", "Almoço: Salada com frango", "Jantar: Sopa de legumes"]
    },
}

alimentacao = {
    "2024-06-27": {
        "meta_carboidratos": 300,
        "meta_proteinas": 150,
        "meta_gorduras": 70,
        "meta_kcal": 2000
    },
}