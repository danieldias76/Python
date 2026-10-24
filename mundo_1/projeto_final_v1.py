print("=============================")
print("     SISTEMA DE CAIXA        ")
print("=============================")

produto = input('Produto:')
preco = float(input('Preço: R$ '))
qtd = int(input('Quantidade:'))

total = preco * qtd
print(f'Subtotal: R${total:.2f}\n')

print('Forma de pagamento:')
print('1 - Dinheiro (Desconto de 10%)')
print('2 - Pix (Desconto de 15%)')
print('3 - Cartão (Acréscimo de 15%)')

desconto_Dinheiro = total * (10 / 100)
valor_Final_Dinheiro = total - desconto_Dinheiro

desconto_Pix = total * (15 / 100)
valor_Final_Pix = total - desconto_Pix

acrescimo_Cartao = total * (15 / 100)
valor_Final_Cartao = total + acrescimo_Cartao

mtdPgto = int(input('Escolha:'))

if mtdPgto == 1:
    print(f'Método de pagamento em Dinheiro, desconto de R${desconto_Dinheiro:.2f}, '
          f'valor final da compra R${valor_Final_Dinheiro:.2f}')
elif mtdPgto == 2:
    print(f'Método de pagamento em Pix, desconto de R${desconto_Pix:.2f} '
          f'valor final da compra R${valor_Final_Pix:.2f}')
elif mtdPgto == 3:
    print(f'Método de pagamento em Cartão, desconto de R${acrescimo_Cartao:.2f}'
          f'valor final da compra R${valor_Final_Cartao:.2f}')
else:
    print('Opção inválida!')
# print('TABELA DE DESCONTOS')
# print('R$100              -> sem desconto')
# print('R$100 até R$299    -> 5%')
# print('R$300 até R$499    -> 10%')
# print('R$500 ou mais      ->')
# Cartão  -> 15% acréscimo
# Pix     -> 15% desconto
# Dinheiro -> 10% desconto