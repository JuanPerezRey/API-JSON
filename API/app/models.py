from pydantic import BaseModel

class Telefono(BaseModel):
    marca: str
    modelo: str
    almacenamiento_gb: str
    color: str
    precio: int
    stock: int
    codigo_telefono: int