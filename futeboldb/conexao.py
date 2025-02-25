from pymongo import MongoClient

# Substitua pelos seus dados de conexão
uri = ""

# Criar função para obter a conexão
def get_db():
    client = MongoClient(uri)
    db = client["FutebolDB"]
    return db
