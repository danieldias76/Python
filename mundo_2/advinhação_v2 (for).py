import random

print('=== JOGO DA ADVINHAÇÃO V2 (for) ===')

# Inicialização do número sorteado pela máquina
numero_sorteado = random.randint(1, 10)

# ==========================================
# TÓPICO 1: Laço de repetição limitado (Permite até 10 tentativas)
# ==========================================
for i in range(1, 11):

    # ------------------------------------------
    # TÓPICO 2: Leitura do palpite do usuário
    # ------------------------------------------
    n = int(input('Digite um número para começar (1/10): '))

    # ------------------------------------------
    # TÓPICO 3: Verificação de dicas e condição de vitória
    # ------------------------------------------
    if n > numero_sorteado:
        print(f'Numero é menor')
    elif n < numero_sorteado:
        print(f'Numero é maior')
    else:
        print(f'Parabéns! Você acertou!')
        print(f'Você precisou de {i} tetantiva(s) para vencer!')
        break  # Encerra o loop antecipadamente se o jogador acertar
else:
    # ------------------------------------------
    # TÓPICO 4: Bloco executado caso o jogador esgote todas as tentativas sem acertar
    # ------------------------------------------
    print('Suas tentativas acabaram! Jogo encerrado.')
    print(f'O número secreto era: {numero_sorteado}')