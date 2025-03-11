from conexao import get_db

# Obter o banco de dados
db = get_db()
jogadores_collection = db["jogadores"]

# Atualizar o vigor físico do jogador "Cristiano Ronaldo"
resultado = jogadores_collection.update_one(
    {"Nome": "Cristiano Ronaldo"},  # Critério de busca
    {"$set": {"saude.Vigor_Fisico_Semana": "Bom"}}  # Atualização
)

print(f"Jogadores modificados: {resultado.modified_count}")
