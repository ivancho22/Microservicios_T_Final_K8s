
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

ventas = []

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    total = sum(v["valor"] for v in ventas)
    return templates.TemplateResponse("index.html", {"request": request, "ventas": ventas, "total": total})

@app.post("/vender", response_class=HTMLResponse)
def vender(request: Request, nombre: str = Form(...), valor: float = Form(...), idx: int = Form(-1)):
    if idx >= 0:
        ventas[idx] = {"nombre": nombre, "valor": valor}
    else:
        ventas.append({"nombre": nombre, "valor": valor})
    return RedirectResponse("/", status_code=303)

@app.get("/eliminar/{idx}")
def eliminar(idx: int):
    if 0 <= idx < len(ventas):
        ventas.pop(idx)
    return RedirectResponse("/", status_code=303)

@app.get("/editar/{idx}", response_class=HTMLResponse)
def editar(request: Request, idx: int):
    total = sum(v["valor"] for v in ventas)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "ventas": ventas,
        "total": total,
        "edit_idx": idx,
        "edit_venta": ventas[idx]
    })



## ---> EXECUTE MICROSERVICE  cd ..
## uvicorn app.main:app --reload --port 3300  http://localhost:3300

