from fastapi import HTTPException
from conexao_neo4j import conn

def detectar_comunidades():
    try:
        # Query 100% compatível com seu banco
        query = """
        // 1. Primeiro verifica quais labels existem
        MATCH (n)
        WITH DISTINCT labels(n) AS labels
        UNWIND labels AS label
        RETURN COLLECT(label) AS existing_labels;
        """
        
        # Executa para debug - remova depois de confirmar
        labels = conn.query(query)
        print("Labels existentes no banco:", labels[0]["existing_labels"] if labels else "Nenhum")
        
        # Query principal corrigida
        query = """
        // Agrupa jogadores que compartilham posições
        MATCH (j1)-[:JOGA_COMO]->(pos:Posicao)<-[:JOGA_COMO]-(j2)
        WHERE elementId(j1) < elementId(j2)  // Substitui o id() depreciado
        WITH pos.nome AS posicao, COLLECT(j1) + COLLECT(j2) AS grupo_jogadores
        UNWIND grupo_jogadores AS j
        WITH posicao, COLLECT(DISTINCT j) AS comunidade_jogadores
        RETURN posicao AS Comunidade, 
               [j IN comunidade_jogadores | j.Nome] AS Jogadores
        ORDER BY SIZE(comunidade_jogadores) DESC
        """
        
        resultados = conn.query(query)
        if not resultados:
            raise Exception("Nenhum resultado encontrado. Verifique os labels dos nós.")
        
        # Reformatação da saída
        comunidades_formatadas = []
        for idx, record in enumerate(resultados):
            for jogador in record["Jogadores"]:
                comunidades_formatadas.append({
                    "Jogador": jogador,
                    "Comunidade": idx
                })
        
        return comunidades_formatadas
        
    except Exception as e:
        print("Erro detalhado no Neo4j:", e)
        raise HTTPException(
            status_code=500,
            detail=f"Erro na análise: {str(e)}. Verifique os logs do servidor."
        )