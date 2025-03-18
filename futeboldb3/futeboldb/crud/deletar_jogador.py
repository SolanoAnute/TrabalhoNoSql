from conexao import get_db  

def deletar_jogador(jogador_id):
    db = get_db()
    jogadores_collection = db["jogadores"]

    resultado = jogadores_collection.delete_one({"ID": jogador_id})
    return resultado.deleted_count > 0  # Retorna True se um jogador foi deletado
