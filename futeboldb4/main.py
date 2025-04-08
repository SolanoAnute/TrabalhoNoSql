from fastapi import FastAPI
from routers import jogadores
from conexao import criar_indices
app = FastAPI()

app.include_router(jogadores.router)

@app.get("/")
def home():
    return {"message": "API de Gerenciamento de Jogadores está rodando!"}




# Criar índices ao iniciar a aplicação
criar_indices()