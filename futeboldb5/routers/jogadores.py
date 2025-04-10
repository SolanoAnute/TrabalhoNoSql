from fastapi import APIRouter, HTTPException
from models import Jogador
from crud.inserir_jogador import inserir_jogador
from crud.listar_jogadores import listar_jogadores
from crud.atualizar_jogador import atualizar_jogador
from crud.deletar_jogador import deletar_jogador
from crud.listar_jogadores import contar_jogadores_por_posicao
from crud.listar_jogadores import analisar_jogadores_com_queixa
from crud.listar_jogadores import contar_jogadores_veteranos
from crud.listar_jogadores import listar_indices
from conexao_neo4j import conn
from analise_grafos import detectar_comunidades
from analise_grafos import detectar_comunidades_gds as detectar_comunidades


router = APIRouter()

@router.get("/jogadores/comunidades")
def obter_comunidades():
    return detectar_comunidades()

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


@router.get("/jogadores/contagem-posicao/")
def obter_contagem_jogadores():
    return contar_jogadores_por_posicao()









@router.get("/jogadores/queixas/")
def obter_jogadores_com_queixa():
    return analisar_jogadores_com_queixa()




@router.get("/jogadores/veteranos/")
def obter_jogadores_veteranos():
    return contar_jogadores_veteranos()


@router.get("/jogadores/indices/")
def obter_indices():
    return listar_indices()

@router.get("/jogadores/{jogador_id}/relacionados")
def obter_jogadores_relacionados(jogador_id: int):
    query = """
    MATCH (j1:Jogador {ID: $ID})-[:JOGA_COMO]->(pos)<-[:JOGA_COMO]-(j2:Jogador)
    WHERE j1 <> j2
    RETURN j2.ID as ID, j2.Nome as Nome, pos.nome as PosicaoComum
    """
    resultados = conn.query(query, {"ID": jogador_id})
    if not resultados:
        raise HTTPException(status_code=404, detail="Jogador não encontrado ou sem relacionamentos")
    return [dict(r) for r in resultados]


@router.get("/jogadores/analise-quimica")
def analise_quimica_time():
    query = """
    MATCH (j1:Jogador)-[:JOGA_COMO]->(pos)<-[:JOGA_COMO]-(j2:Jogador)
    WHERE j1.ID < j2.ID
    RETURN j1.Nome as Jogador1, j2.Nome as Jogador2, pos.nome as PosicaoComum,
           COUNT(*) as ForcaConexao
    ORDER BY ForcaConexao DESC
    LIMIT 10
    """
    resultados = conn.query(query)
    return [dict(r) for r in resultados]
