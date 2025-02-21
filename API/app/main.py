from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from app.routes.telefonos import telefonos_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/templates"), name="static")

app.include_router(telefonos_router)

@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API de la Universidad"}