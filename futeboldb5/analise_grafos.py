from fastapi import HTTPException
from conexao_neo4j import conn

def criar_projecao_grafo():
    """Cria a projeção do grafo necessária para os algoritmos GDS"""
    try:
        query = """
        // Verifica se a projeção já existe
        CALL gds.graph.exists('jogadoresPosicoes') 
        YIELD exists
        WHERE NOT exists
        CALL gds.graph.project(
            'jogadoresPosicoes',
            ['jogador', 'Posicao'],
            'JOGA_COMO',
            {
                nodeProperties: ['Nome', 'Posicao_Origem'],
                relationshipProperties: {}
            }
        )
        YIELD graphName, nodeCount, relationshipCount
        RETURN graphName, nodeCount, relationshipCount
        """
        return conn.query(query)
    except Exception as e:
        raise Exception(f"Falha ao criar projeção: {str(e)}")

def detectar_comunidades_gds():
    try:
        # 1. Cria a projeção do grafo (se não existir)
        criar_projecao_grafo()

        # 2. Executa o algoritmo Louvain com GDS
        query = """
        CALL gds.louvain.stream('jogadoresPosicoes', {
            includeIntermediateCommunities: false,
            relationshipTypes: ['JOGA_COMO']
        })
        YIELD nodeId, communityId
        WITH gds.util.asNode(nodeId) AS jogador, communityId
        WHERE 'jogador' IN labels(jogador)  // Filtra apenas nós de jogador
        RETURN {
            Jogador: jogador.Nome,
            Comunidade: communityId,
            Posicao: jogador.Posicao_Origem
        } AS resultado
        ORDER BY communityId, jogador.Nome
        """
        
        resultados = conn.query(query)
        
        if not resultados:
            raise Exception("Nenhum resultado encontrado. Verifique os dados.")
        
        # Formatação da resposta
        return [dict(record["resultado"]) for record in resultados]
        
    except Exception as e:
        print(f"Erro no GDS: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Falha na análise: {str(e)}"
        )
