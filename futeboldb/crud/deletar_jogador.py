from conexao import get_db

# Obter o banco de dados
db = get_db()
jogadores_collection = db["jogadores"]

# Deletar jogador
resultado = jogadores_collection.delete_one({"Nome": 'Vinicius Junior'})

print(f"Jogadores deletados: {resultado.deleted_count}")
