from fastapi import FastAPI
from backendpython import personas
from fastapi.middleware.cors import CORSMiddleware
from backendpython.src.conexion_postgresql import check_and_create_table

app = FastAPI()

check_and_create_table()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir estos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.include_router(personas.router)

@app.get("/")
async def root():
    return {"message":"Hello World"}

