from conexao import get_db  

def inserir_jogador(jogador):
    db = get_db()
    jogadores_collection = db["jogadores"]

    # Inserir jogador (usando o objeto jogador passado como parâmetro)
    resultado = jogadores_collection.insert_one(jogador.dict())  # Converte o objeto Pydantic para dicionário
    print(f"Jogador inserido com ID: {resultado.inserted_id}")  # Exibe o ID inserido
    return str(resultado.inserted_id)  # Retorna o ID inserido
