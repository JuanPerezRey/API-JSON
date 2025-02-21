from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models import Telefono
import json
import os

telefonos_router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

DATA_FILE = "app/data/telefonos.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

@telefonos_router.get("/", response_class=HTMLResponse)
async def read_telefonos(request: Request):
    telefonos = load_data()
    return templates.TemplateResponse("index.html", {"request": request, "telefonos": telefonos})

@telefonos_router.get("/crear", response_class=HTMLResponse)
async def crear_Telefono_form(request: Request):
    return templates.TemplateResponse("crear_telefono.html", {"request": request})

@telefonos_router.post("/crear")
async def crear_telefono(telefonos: Telefono):
    data = load_data()
    data.append(telefonos.model_dump())
    save_data(data)
    return {"message": "Telefono agregado exitosamente"}

@telefonos_router.get("/buscar")
async def buscar_telefono(request: Request, codigo_telefono: int):
    telefonos = load_data()
    telefono = next((e for e in telefonos if e["codigo_telefono"] == codigo_telefono), None)
    if telefono:
        return templates.TemplateResponse("buscar_telefono.html", {"request": request, "telefono": telefono})
    else:
        raise HTTPException(status_code=404, detail="Telefono no encontrado")
