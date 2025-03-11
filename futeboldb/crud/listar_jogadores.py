from conexao import get_db

# Obter o banco de dados
db = get_db()
jogadores_collection = db["jogadores"]

# Buscar jogadores
jogadores = jogadores_collection.find()

# Exibir jogadores
print("\nJogadores cadastrados no banco de dados:")
for jogador in jogadores:
    print(jogador)
