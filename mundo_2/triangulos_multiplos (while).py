print("=======================================")
print("   BEM-VINDO AO VERIFICADOR DE RETAS   ")
print("=======================================")

while True:
    print("\nEscolha uma opção:")
    print("1 - Testar um conjunto de retas (triângulo)")
    print("2 - Sair do programa")

    opcao = input("Digite o número da sua escolha: ")

    if opcao == "1":
        print("\n--- Novo Teste ---")
        a = float(input("Digite o valor do 1º lado: "))
        b = float(input("Digite o valor do 2º lado: "))
        c = float(input("Digite o valor do 3º lado: "))

        # Verificação da desigualdade triangular
        if (a + b > c) and (a + c > b) and (b + c > a):
            print("-> Os lados formam um triângulo VÁLIDO!")
        else:
            print("-> Os lados NÃO formam um triângulo.")

    elif opcao == "2":
        print("\nEncerrando o programa. Até a próxima!")
        break

    else:
        print("\n⚠️ Opção inválida! Digite '1' para testar ou '2' para sair.")