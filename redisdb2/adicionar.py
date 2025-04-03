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
    
    # BITMAP: Define o bit correspondente ao jogador (1 para "Apto", 0 caso contrário)
    offset = int(r.incr("contador:jogadores"))  
    r.setbit("status:aptos", offset, 1 if status_fisico == "Apto" else 0)
    
    print(f"Jogador '{nome}' adicionado! Bitmap atualizado no offset {offset}.")
    r.bf().add("bloom:jogadores", nome.lower())


if __name__ == "__main__":
    adicionar_jogador("Neymar", "Atacante", 32, "Apto")