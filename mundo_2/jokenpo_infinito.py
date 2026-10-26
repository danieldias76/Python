import random

# Inicialização das variáveis de controle de placar e estatísticas
placarPc = 0
placarJogador = 0
jogadas = 0
empates = 0

print("Escolhe entre:\n"
      "1 - PEDRA\n"
      "2 - PAPEL\n"
      "3 - TESOURA\n")

# ==========================================
# TÓPICO 1: Laço principal do jogo (Gerencia as rodadas)
# ==========================================
while True:
    # ------------------------------------------
    # TÓPICO 2: Verificação do limite de jogadas
    # ------------------------------------------
    if jogadas >= 5:
        print("Fim de jogo! Limite de jogadas atingido.")
        break

    # ------------------------------------------
    # TÓPICO 3: Entrada da escolha do jogador e contagem de jogadas
    # ------------------------------------------
    escolhaJogador = int(input("Qual foi sua escolha? "))
    jogadas += 1

    # ------------------------------------------
    # TÓPICO 4: Jogada aleatória do computador
    # ------------------------------------------
    escolhaPc = random.randint(1, 3)

    # ------------------------------------------
    # TÓPICO 5: Verificação de empate, vitória do jogador ou vitória do computador
    # ------------------------------------------
    if escolhaJogador == escolhaPc:
        empates += 1
        print(f'Empate! Os dois escolheram {escolhaJogador}\n')

    elif    (escolhaJogador == 1 and escolhaPc == 3) or \
            (escolhaJogador == 2 and escolhaPc == 1) or \
            (escolhaJogador == 3 and escolhaPc == 2) :

        placarJogador += 1
        print(f"Jogador venceu, com: {escolhaJogador}")
        print(f"Escolha do Pc foi {escolhaPc}")
        break  # Encerra o jogo quando o jogador vence

    else:
        placarPc += 1
        print(f"Pc venceu com {escolhaPc}")
        print(f"Jogador escolheu {escolhaJogador}")

# ==========================================
# TÓPICO 6: Exibição do placar e estatísticas finais
# ==========================================
print("\n--- PLACAR FINAL ---")
print(f"Vitórias do Jogador: {placarJogador}")
print(f"Vitórias do PC: {placarPc}")
print(f"Empates: {empates}")
print(f"Total de jogadas: {jogadas}")