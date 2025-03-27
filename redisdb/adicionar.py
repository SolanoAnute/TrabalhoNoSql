from conexao import get_redis_connection

def adicionar_jogador(nome, posicao, idade, status_fisico):
    r = get_redis_connection()
    chave = f"jogador:{nome.lower()}"
    r.hset(chave, mapping={
        "nome": nome,
        "posicao": posicao,
        "idade": idade,
        "status_fisico": status_fisico
    })
    print(f"Jogador '{nome}' adicionado com sucesso!")

# Teste
if __name__ == "__main__":
    adicionar_jogador("Neymar", "Atacante", 32, "Apto")
