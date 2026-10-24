import random

print('=== JOGO DA ADVINHAÇÃO V2 (for) ===')

numero_sorteado = random.randint(1,10)

for i in range(1,11):
    n = int(input('Digite um número para começar (1/10):'))
    if n > numero_sorteado:
        print(f'Numero é menor')
    elif n < numero_sorteado:
        print(f'Numero é maior')
    else:
        print(f'Parabéns! Você acertou!')
        print(f'Você precisou de {i} tetantiva(s) para vencer!')
        break
else:
    print('Suas tentativas acabaram! Jogo encerrado.')
    print(f'O número secreto era: {numero_sorteado}')
