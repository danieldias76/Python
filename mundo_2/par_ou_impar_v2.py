import random

# Inicializa a contagem de vitórias consecutivas do jogador
winstreak = 0

print("====================================")
print("          Par ou Ímpar V2           ")
print("====================================")

# ==========================================
# TÓPICO 1: Laço principal do jogo (Gerencia as rodadas)
# ==========================================
while True:

    # ------------------------------------------
    # TÓPICO 2: Laço de validação da escolha (P, I ou S)
    # ------------------------------------------
    while True:
        tipo = input('Par ou Ímpar? [P/I] (ou S para sair): ').strip().upper()

        if tipo == 'P':
            print('Você escolheu par!')
            break
        elif tipo == 'I':
            print('Você escolheu impar!')
            break
        elif tipo == 'S':
            print('Encerrando o programa... Até logo!')
            exit()  # Encerra o script completamente
        else:
            print('Opção inválida! Digite P, I ou S.')

    # ------------------------------------------
    # TÓPICO 3: Laço de validação do número do jogador (Restrito à escolha)
    # ------------------------------------------
    while True:
        n = int(input('Digite um número inteiro: '))

        if tipo == 'P' and n % 2 == 0:
            print(f'Você escolheu par e jogou {n}. Válido!')
            break
        elif tipo == 'I' and n % 2 != 0:
            print(f'Você escolheu impar e jogou {n}. Válido!')
            break
        else:
            print('Número inválido para a sua escolha! Tente novamente.')

    # ------------------------------------------
    # TÓPICO 4: Jogada do computador e cálculo do resultado da rodada
    # ------------------------------------------
    pcPick = random.randint(1, 10)
    soma = n + pcPick

    # ------------------------------------------
    # TÓPICO 5: Verificação de vitória ou derrota e atualização do winstreak
    # ------------------------------------------
    if (soma % 2 == 0 and tipo == 'P') or (soma % 2 != 0 and tipo == 'I'):
        winstreak += 1
        print(f'O computador jogou {pcPick}. A soma deu {soma}.')
        print(f'Você ganhou! Sequência de {winstreak} vitória(s).\n')
        # O jogo retorna ao início do Tópico 1 automaticamente para a próxima rodada
    else:
        resultado_str = 'Par' if soma % 2 == 0 else 'Ímpar'
        print(f'O computador jogou {pcPick}. A soma deu {soma} ({resultado_str}).')
        print(f'Você perdeu! Fim de jogo. Sua sequência final foi de {winstreak} vitória(s).')
        break  # Quebra o laço principal (Tópico 1) e encerra o jogo