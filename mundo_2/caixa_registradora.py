print('=' * 3 + ' Simulador de Compra ' + 3 * '=')

totgasto, tot_cem, menor_preco, count = 0, 0, 0, 0
barato = ''

while True:
    produto = str(input('Digite o nome do Produto:')).strip()
    preco = float(input('Informe preço do Produto:(R$)'))
    qtd = int(input('Quantidade do Produto:'))

    # Ajustado o texto da pergunta para ficar intuitivo
    continuar = str(input('Quer continuar?[S/N]:')).strip()
    count += 1

    if (count == 1) or (preco < menor_preco):
        menor_preco = preco
        barato = produto

    total = preco * qtd
    totgasto += total
    print('=' * 10)
    print(f'Subtotal:R${total:.2f}\n')

    if preco > 100:
        tot_cem += 1

    # CORREÇÃO: O programa agora só encerra se o usuário digitar 'n' (Não)
    if continuar.lower() == 'n':
        print('Compra confirmada!')
        break

# --- O QUE FALTAVA: EXIBIÇÃO DOS RESULTADOS FINAIS (FORA DO WHILE) ---
print('\n' + '=' * 30)
print('FIM DO PROGRAMA E RESUMO DA COMPRA')
print(f'O total gasto na compra foi R$ {totgasto:.2f}')
print(f'Tivemos {tot_cem} produto(s) custando mais de R$ 100,00')
print(f'O produto mais barato foi {barato} custando R$ {menor_preco:.2f}')
print('=' * 30)