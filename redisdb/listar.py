from conexao import get_redis_connection

def listar_jogadores():
    r = get_redis_connection()
    chaves = r.keys("jogador:*")
    jogadores = [r.hgetall(chave) for chave in chaves]
    return jogadores

# Teste
if __name__ == "__main__":
    print(listar_jogadores())
