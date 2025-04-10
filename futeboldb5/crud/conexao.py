from pymongo import MongoClient

# Substitua pelos seus dados de conexão
uri = "mongodb+srv://solanute:123@cluster0.fpr24.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Criar função para obter a conexão
def get_db():
    client = MongoClient(uri)
    db = client["FutebolDB"]
    return db

def criar_indices():
    db = get_db()
    jogadores_collection = db["jogadores"]

    # Criando um índice no campo Posicao_Origem para otimizar consultas
    jogadores_collection.create_index("Posicao_Origem")