print('=' * 5 + ' Triângulos Multiplos (For) ' + 5 * '=')
quantidade = int(input("Quantos triângulos deseja verificar? "))

count = 0
historico = ""

for i in range(quantidade):
    # Lê os três lados do triângulo atual
    a, b, c = map(float, input(f"Digite os 3 lados do triângulo {i + 1} (separados por espaço): ").split())

    count += 1

    # Calcula a soma dos valores dos lados deste triângulo
    soma_lados = a + b + c

    # Verifica a condição de existência do triângulo e inclui a soma no texto
    if (a + b > c) and (a + c > b) and (b + c > a):
        resultado = f"Triângulo {i + 1} (Lados: {a}, {b}, {c}) | Soma dos lados: {soma_lados} -> É VÁLIDO."
    else:
        resultado = f"Triângulo {i + 1} (Lados: {a}, {b}, {c}) | Soma dos lados: {soma_lados} -> NÃO é válido."

    historico += resultado + "\n"

# Exibe o painel final
print("\n" + "=" * 5 + " RESUMO FINAL DOS TESTES " + "=" * 5)
print(historico)
print(f"Total de Triângulos verificados: {count}")