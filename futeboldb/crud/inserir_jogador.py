from conexao import get_db  # Importa a conexão

# Obter o banco de dados
db = get_db()
jogadores_collection = db["jogadores"]

# Criar um novo jogador
jogador = {
    "ID": 2, 
    "Nome": "Vinicius Junior",
    "Data_Nascimento": "2000-06-12",
    "Posicao_Origem": "Atacante",
    "Posicoes_Complementares": [" Meia-Atacante"],
    "Tempo_Jogado_Semana": 180,
    "saude": {
        "Vigor_Fisico_Semana": "Bom",
        "Queixa_Problemas_Semana": "Nenhuma",
        "Condicao_Jogo_Semana": "Disponível",
        "Capacidade_Jogo": "Metade partida",
        "Status_Tratamento_Lesao": "Sem lesão"
    }
}

# Inserir jogador
resultado = jogadores_collection.insert_one(jogador)
print(f"Jogador inserido com ID: {resultado.inserted_id}")
