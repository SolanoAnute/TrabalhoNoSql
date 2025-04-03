from conexao import get_redis_connection

def obter_jogador(nome):
    r = get_redis_connection()
    chave = f"jogador:{nome.lower()}"
    
    # BLOOM FILTER: Verifica se o jogador POTENCIALMENTE existe
    if not r.bf().exists("bloom:jogadores", nome):
        return f"Jogador '{nome}' não encontrado (filtro Bloom)."
    
    # Se passar pelo filtro, busca no Redis
    jogador = r.hgetall(chave)
    return jogador if jogador else f"Jogador '{nome}' não encontrado."


if __name__ == "__main__":
    print(obter_jogador("Neymar"))