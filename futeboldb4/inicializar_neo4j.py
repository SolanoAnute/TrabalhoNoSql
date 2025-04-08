def importar_jogadores_do_mongodb():
    from conexao import get_db
    from datetime import datetime
    
    db = get_db()
    jogadores_mongo = db["jogadores"].find()
    
    for jogador in jogadores_mongo:
        # Extrair década da data de nascimento
        ano_nascimento = int(jogador["Data_Nascimento"][:4])
        decada = (ano_nascimento // 10) * 10
        
        # Criar nó do jogador com propriedades organizadas
        query = """
        MERGE (j:Jogador {ID: $ID})
        SET j.Nome = $Nome,
            j.name = $Nome,  
            j.Data_Nascimento = $Data_Nascimento,
            j.Decada = $Decada,
            j.Posicao_Origem = $Posicao_Origem,
            j.label = 'Jogador'
        """
        params = {
            "ID": jogador["ID"],
            "Nome": jogador["Nome"],
            "Data_Nascimento": jogador["Data_Nascimento"],
            "Decada": decada,
            "Posicao_Origem": jogador["Posicao_Origem"]
        }
        conn.query(query, params)