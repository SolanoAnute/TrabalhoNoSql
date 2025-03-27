from conexao import get_redis_connection

def atualizar_jogador(nome, campo, novo_valor):
    r = get_redis_connection()
    chave = f"jogador:{nome.lower()}"
    if r.exists(chave):
        r.hset(chave, campo, novo_valor)
        print(f"Jogador '{nome}' atualizado: {campo} -> {novo_valor}")
    else:
        print(f"Jogador '{nome}' não encontrado.")


if __name__ == "__main__":
    atualizar_jogador("Neymar", "status_fisico", "Lesionado")
