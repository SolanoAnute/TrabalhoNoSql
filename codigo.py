from pymongo import MongoClient

# Substitua pela sua string de conexão
uri = "mongodb+srv://solanute:123@cluster0.fpr24.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Criar uma conexão com o MongoDB
client = MongoClient(uri)

# Acessar o banco de dados 
db = client["futebolDB"]

# Acessar a coleção de jogadores
jogadores = db["jogadores"]

# Criar um banco de dados chamado "FutebolDB"
db = client["FutebolDB"]

# Criar uma coleção chamada "jogadores"
collection = db["jogadores"]

# 4️⃣ Inserir um novo jogador
novo_jogador = {"nome": "Cristiano Ronaldo", "idade": 39, "posição": "Atacante", "clube": "Al-Nassr", }
collection.insert_one(novo_jogador)

# 7️⃣ Remover um jogador
#collection.delete_one({"nome": "Neymar"})


jogadores = collection.find()
for jogador in jogadores:
    print(jogador)



