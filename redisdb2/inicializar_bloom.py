from conexao import get_redis_connection

def inicializar_bloom():
    r = get_redis_connection()
    
    # Cria o Bloom Filter se não existir (com taxa de falso positivo de 1%)
    try:
        r.bf().create("bloom:jogadores", 0.01, 1000)
        print("Bloom Filter 'bloom:jogadores' criado!")
    except Exception as e:
        print(f"Bloom Filter já existe ou erro: {e}")

    # Adiciona jogadores existentes ao filtro (sem .decode()!)
    chaves = r.keys("jogador:*")
    for chave in chaves:
        nome = chave.split(":")[1]  # Remove .decode() pois já é string
        r.bf().add("bloom:jogadores", nome.lower())

if __name__ == "__main__":
    inicializar_bloom()