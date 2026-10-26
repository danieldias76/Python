import random

print('=== JOGO DA ADVINHAÇÃO V2 (while) ===')

# Inicialização do número secreto e das variáveis de controle
numero_secreto = random.randint(1, 10)
palpite = 0
tentativas = 0

# ==========================================
# TÓPICO 1: Laço principal do jogo (Repete até o jogador acertar)
# ==========================================
while palpite != numero_secreto:

    # ------------------------------------------
    # TÓPICO 2: Leitura do palpite do usuário e contagem de tentativas
    # ------------------------------------------
    palpite = int(input("Qual é o seu palpite (entre 1 e 10)? "))
    tentativas += 1

    # ------------------------------------------
    # TÓPICO 3: Verificação e dicas (Maior, Menor ou Acertou)
    # ------------------------------------------
    if palpite > numero_secreto:
        print('Errou! O número secreto é menor.')
    elif palpite < numero_secreto:
        print('Errou! O número secreto é maior.')
    else:
        print(f'Acertou! O número é {numero_secreto}')
        print(f'Foram {tentativas} de tentativa(s) para acertar')
        # O loop termina automaticamente aqui porque a condição (palpite != numero_secreto) deixa de ser verdadeira