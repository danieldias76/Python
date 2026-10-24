import random

print('=== JOGO DA ADVINHAÇÃO V2 (while) ===')

numero_secreto = random.randint(1,10)

palpite = 0
tentativas = 0

while palpite != numero_secreto:
    palpite = int(input("Qual é o seu palpite (entre 1 e 10)? "))
    tentativas += 1

    if palpite > numero_secreto:
        print('Errou! O número secreto é menor.')
    elif palpite < numero_secreto:
        print('Errou! O número secreto é maior.')
    else:
        print(f'Acertou! O número é {numero_secreto}')
        print(f'Foram {tentativas} de tentativa(s) para acertar')
