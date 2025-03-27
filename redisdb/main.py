from adicionar import adicionar_jogador
from obter import obter_jogador
from listar import listar_jogadores
from atualizar import atualizar_jogador
from deletar import deletar_jogador

adicionar_jogador("Messi", "Atacante", 37, "Apto")
adicionar_jogador("Cristiano", "Atacante", 40, "Cansado")

print("\nObtendo Messi:")
print(obter_jogador("Messi"))

print("\nListando jogadores:")
print(listar_jogadores())

print("\nAtualizando status físico de Cristiano Ronaldo:")
atualizar_jogador("Cristiano", "status_fisico", "Apto")

print("\nDeletando Messi:")
deletar_jogador("Messi")

print("\n Listando jogadores após exclusão:")
print(listar_jogadores())
