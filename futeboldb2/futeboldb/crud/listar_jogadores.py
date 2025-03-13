from conexao import get_db  

def listar_jogadores():
    db = get_db()
    jogadores_collection = db["jogadores"]

    jogadores = list(jogadores_collection.find({}, {"_id": 0}))  # Remove o _id do MongoDB para evitar erro de conversão
    
    print("Jogadores cadastrados:")
    for jogador in jogadores:
        print(jogador)
    
    return jogadores