from pymongo import MongoClient

# Substitua pelos seus dados de conexão
uri = "mongodb+srv://solanute:123@cluster0.fpr24.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Criar função para obter a conexão
def get_db():
    client = MongoClient(uri)
    db = client["FutebolDB"]
    return db