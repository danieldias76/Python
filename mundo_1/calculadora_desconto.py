c = float(input('Informe o valor da compra:R$').strip())
print(f'Compra de R${c:.2f}')

d = c * ( 15 / 100)

if c >= 500:
    print(f'Compra com desconto aceita!')
    print(f'Compra acima ou igual de R$500,00 desconto de {d:.2f}')
    print(f'Valor final da compra: R${c - d:.2f}')
else:
    print(f'Desconto apenas acima de R$500')
    print(f'Valor total da compra {c:.2f}')


