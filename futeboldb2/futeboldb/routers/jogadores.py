from fastapi import APIRouter, HTTPException
from models import Jogador
from crud.inserir_jogador import inserir_jogador
from crud.listar_jogadores import listar_jogadores
from crud.atualizar_jogador import atualizar_jogador
from crud.deletar_jogador import deletar_jogador

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

from typing import List  # Importe List para usar no tipo de parâmetro
from models import Jogador  # Certifique-se de que Jogador seja o modelo Pydantic

@router.post("/jogadores/inserir-lote/")
def criar_jogadores_em_lote(jogadores: List[Jogador]):
    ids_inseridos = []
    for jogador in jogadores:
        jogador_id = inserir_jogador(jogador)
        ids_inseridos.append(jogador_id)
    return {"message": "Jogadores inseridos com sucesso!", "ids_inseridos": ids_inseridos}