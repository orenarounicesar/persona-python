from pydantic import BaseModel
from typing import Optional
from datetime import date

class Persona(BaseModel):
    id: Optional[int] = None
    tipo_identificacion: str
    numero_identificacion: str
    nombre1: str
    nombre2: str
    apellido1: str
    apellido2: str
    sexo: str
    fecha_nacimiento: date
    