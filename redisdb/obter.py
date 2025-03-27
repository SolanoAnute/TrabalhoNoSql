from conexao import get_redis_connection

def obter_jogador(nome):
    r = get_redis_connection()
    chave = f"jogador:{nome.lower()}"
    jogador = r.hgetall(chave)
    return jogador if jogador else f"Jogador '{nome}' não encontrado."

# Teste
if __name__ == "__main__":
    print(obter_jogador("Neymar"))
