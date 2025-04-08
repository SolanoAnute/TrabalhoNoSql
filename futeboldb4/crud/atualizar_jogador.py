from conexao import get_db  

def atualizar_jogador(jogador_id, novos_dados):
    db = get_db()
    jogadores_collection = db["jogadores"]
    
    resultado = jogadores_collection.update_one(
        {"ID": jogador_id},  
        {"$set": novos_dados.dict()}
    )
    
    return resultado.modified_count > 0  # Retorna True se algo foi modificado
