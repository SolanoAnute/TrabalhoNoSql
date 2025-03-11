from fastapi import APIRouter, HTTPException
from models import Jogador
from crud import inserir_jogador, listar_jogadores, atualizar_jogador, deletar_jogador

router = APIRouter()

@router.post("/jogadores/")
def criar_jogador(jogador: Jogador):
    jogador_id = inserir_jogador(jogador)
    return {"message": "Jogador inserido!", "id": jogador_id}

@router.get("/jogadores/")
def obter_jogadores():
    return listar_jogadores()

@router.put("/jogadores/{jogador_id}")
def modificar_jogador(jogador_id: int, novos_dados: Jogador):
    if atualizar_jogador(jogador_id, novos_dados):
        return {"message": "Jogador atualizado!"}
    raise HTTPException(status_code=404, detail="Jogador não encontrado.")

@router.delete("/jogadores/{jogador_id}")
def remover_jogador(jogador_id: int):
    if deletar_jogador(jogador_id):
        return {"message": "Jogador removido!"}
    raise HTTPException(status_code=404, detail="Jogador não encontrado.")
