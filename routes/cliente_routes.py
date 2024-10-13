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

@router.get("/calendario/{year?}/{month?}", response_class=HTMLResponse)
async def get_calendario(request: Request, year: int = None, month: int = None):
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

# Dados simulados para alimentação
# Simulando alguns dados de alimentação
alimentacao = {
    "2024-10-13": {
        "menu": "Almoço: Arroz, Feijão, Carne Assada, Salada",
        "carboidratos": 200,
        "proteinas": 80,
        "gorduras": 50,
        "calorias_totais": 1500
    },
    "2024-10-14": {
        "menu": "Almoço: Macarrão, Frango Grelhado, Legumes",
        "carboidratos": 220,
        "proteinas": 90,
        "gorduras": 60,
        "calorias_totais": 1600
    }
}

@router.get("/alimentacao", response_class=HTMLResponse)
async def get_alimentacao(request: Request, day: str = None):
    today = date.today().isoformat()  # Use date.today() após corrigir a importação
    if not day:
        day = today
    
    # Obtém os dados de alimentação para o dia especificado
    dados_alimentacao = alimentacao.get(day, {
        "menu": "Informação não disponível",
        "carboidratos": 0,
        "proteinas": 0,
        "gorduras": 0,
        "calorias_totais": 0
    })
    
    # Passa os parâmetros para o template
    context = {
        "request": request,
        "day": day,
        "menu": dados_alimentacao["menu"],
        "carboidratos": dados_alimentacao["carboidratos"],
        "proteinas": dados_alimentacao["proteinas"],
        "gorduras": dados_alimentacao["gorduras"],
        "calorias_totais": dados_alimentacao["calorias_totais"]
    }
    
    # Retorna a resposta do template
    return templates.TemplateResponse("pages/cliente/alimentacao.html", context)

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
