# Inicializa o contador de pessoas cadastradas antes do loop
pessoas = 0

while True:
    # -------------------------------------------------------------
    # 1. ENTRADA DO NOME E VERIFICAÇÃO DE SAÍDA (SENTINELA)
    # -------------------------------------------------------------
    print("=" * 30)
    nome = str(input('Diga seu nome (ou sair para encerrar): ')).strip()

    if nome.lower() == 'sair':
        print('Programa encerrado...')
        break

    # -------------------------------------------------------------
    # 2. ENTRADA E VALIDAÇÃO DA ALTURA
    # -------------------------------------------------------------
    altura = float(input('Informe sua altura: '))

    while altura <= 0:
        print('Altura inválida! Digite um valor maior que zero.')
        altura = float(input('Informe sua altura novamente: '))

    # -------------------------------------------------------------
    # 3. ENTRADA E VALIDAÇÃO DO PESO
    # -------------------------------------------------------------
    peso = float(input('Informe seu peso: '))

    while peso <= 0:
        print('Peso inválido! Digite um valor maior que zero.')
        peso = float(input('Informe seu peso novamente: '))

    # -------------------------------------------------------------
    # 4. CÁLCULO E EXIBIÇÃO DOS RESULTADOS DO IMC
    # -------------------------------------------------------------
    imc = peso / (altura ** 2)

    print('=' * 30)
    print(f'Resultados para: {nome}\n'
          f'Altura: {altura} m\n'
          f'Peso: {peso} kg\n'
          f'IMC de: {imc:.2f}')

    # Classificação encadeada do IMC
    if imc < 18.5:
        print('Status: Abaixo do peso')
    elif 18.5 <= imc <= 24.9:
        print('Status: Peso Ideal')
    elif imc <= 29.9:
        print('Status: Sobrepeso')
    else:
        print('Status: Obesidade')

    # -------------------------------------------------------------
    # 5. ATUALIZAÇÃO DO CONTADOR
    # -------------------------------------------------------------
    # Soma 1 a cada pessoa cadastrada com sucesso
    pessoas += 1

# -------------------------------------------------------------
# 6. RESUMO FINAL APÓS SAIR DO LOOP
# -------------------------------------------------------------
print("\n" + "=" * 30)
print(f"Total de pessoas que informaram o IMC: {pessoas}")
print("=" * 30)