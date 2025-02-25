from pymongo import MongoClient

#string de conexão
uri = ""

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
jogador = {
    "ID": 1,
    "Nome": "João Silva",
    "Data_Nascimento": "1998-05-10",
    "Posicao_Origem": "Meio-Campo Ofensivo",
    "Posicoes_Complementares": ["Atacante"],
    "Tempo_Jogado_Semana": 240,  # em minutos
    "Vigor_Fisico_Semana": "Regular",
    "Queixa_Problemas_Semana": "Não houve",
    "Condicao_Jogo_Semana": "Disponível",
    "Capacidade_Jogo": "Partida Completa",
    "Status_Tratamento_Lesao": "Sem lesão"
}
collection.insert_one(jogador)

# 7️⃣ Remover um jogador
collection.delete_one({"nome": "...."})


jogadores = collection.find()
for jogador in jogadores:
    print(jogador)



