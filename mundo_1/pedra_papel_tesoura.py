import random

print('Digite sua escolha:\n'
      '1 - Pedra\n'
      '2 - Papel\n'
      '3 - Tesoura\n')

escolhaJogador = int(input('Qual vai ser?'))

print(escolhaJogador)

escolhaPc = random.randint(1,3 )

if escolhaJogador == escolhaPc:
    print(f'Empate')
elif    (escolhaJogador == 1 and escolhaPc == 3) or \
        (escolhaJogador == 2 and escolhaPc == 1) or \
        (escolhaJogador == 3 and escolhaPc == 2) :
    print(f'Jogador venceu, com: {escolhaJogador}')
    print(f'Escolha do pc foi: {escolhaPc}')
else:
    print(f'Pc venceu, com: {escolhaPc}')
    print(f'Jogador escolheu: {escolhaJogador}')

