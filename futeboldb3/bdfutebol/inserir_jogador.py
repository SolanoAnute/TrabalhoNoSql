from conexao import get_db  # Importa a conexão

# Obter o banco de dados
db = get_db()
jogadores_collection = db["jogadores"]

# Criar um novo jogador
jogador = {
    "ID": 1, 
    "Nome": "Neymar",
    "Data_Nascimento": "1998-02-05",
    "Posicao_Origem": "Atacante",
    "Posicoes_Complementares": [" Meia-Atacante"],
    "Tempo_Jogado_Semana": 90,
    "saude": {
        "Vigor_Fisico_Semana": "Regular",
        "Queixa_Problemas_Semana": "Dor no joelho esquerdo",
        "Condicao_Jogo_Semana": "Disponível",
        "Capacidade_Jogo": "Metade partida",
        "Status_Tratamento_Lesao": "Treino Regenerativo"
    }
}

# Inserir jogador
resultado = jogadores_collection.insert_one(jogador)
print(f"Jogador inserido com ID: {resultado.inserted_id}")
