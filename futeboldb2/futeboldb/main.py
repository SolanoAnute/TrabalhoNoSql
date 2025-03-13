from fastapi import FastAPI
from routers import jogadores

app = FastAPI()

app.include_router(jogadores.router)

@app.get("/")
def home():
    return {"message": "API de Gerenciamento de Jogadores está rodando!"}
