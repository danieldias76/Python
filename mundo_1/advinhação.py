import random

number = int(input('Informe um número inteiro:')) 

sorteio = random.randint(0,10)

if number == sorteio:
    print(f'{sorteio}')
    print(f'Acertou!{sorteio}')
else:
    print(f'Errou!, resposta:{sorteio}')