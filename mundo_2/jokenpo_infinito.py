import random

placarPc = 0
placarJogador = 0
jogadas = 0
empates = 0

print("Escolhe entre:\n"
      "1 - PEDRA\n"
      "2 - PAPEL\n"
      "3 - TESOURA\n")

while True:
    if jogadas >= 5:
        print("Fim de jogo! Limite de jogadas atingido.")
        break

    escolhaJogador = int((input("Qual foi sua escolha?")))

    jogadas += 1

    escolhaPc = random.randint(1, 3)

    if escolhaJogador == escolhaPc:
        empates += 1
        print(f'Empate! Os dois escolheram {escolhaJogador}\n')

    elif    (escolhaJogador == 1 and escolhaPc == 3) or \
            (escolhaJogador == 2 and escolhaPc == 1) or \
            (escolhaJogador == 3 and escolhaPc == 2) :

        placarJogador += 1
        print(f"Jogador venceu, com :{escolhaJogador}")
        print(f"Escolha do Pc foi {escolhaPc}")
        break

    else:
        placarPc += 1
        print(f"Pc venceu com {escolhaPc}")
        print(f"Jogador escolheu {escolhaJogador}")

print("\n--- PLACAR FINAL ---")
print(f"Vitórias do Jogador: {placarJogador}")
print(f"Vitórias do PC: {placarPc}")
print(f"Empates: {empates}")
print(f"Total de jogadas: {jogadas}")
