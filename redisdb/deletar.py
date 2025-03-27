from conexao import get_redis_connection

def deletar_jogador(nome):
    r = get_redis_connection()
    chave = f"jogador:{nome.lower()}"
    if r.delete(chave):
        print(f"Jogador '{nome}' removido!")
    else:
        print(f"Jogador '{nome}' não encontrado.")

# Teste
if __name__ == "__main__":
    deletar_jogador("Neymar")
