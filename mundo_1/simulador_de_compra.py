print('=== SIMULADOR DE COMPRA ===\n')

produto = input('Nome do Item: ')
preco = float(input('Preço do Item: '))
qtd = int(input('Quantidade:'))
print(f'Produto: {produto}')
print(f'Preço: R${preco:.2f}')
print(f'Quantidade: {qtd}\n')

subtotal = preco * qtd
print(f'Subtotal: R${subtotal:.2f}\n')

print('Forma de pagamento:\n'
      '1 - Dinheiro\n'
      '2 - Pix\n'
      '3 - Cartão\n')

escolhido = int(input('Escolha um meio de pagamento:'))

descontoAvista = (subtotal * 10) / 100
precoAvista = subtotal - descontoAvista
descontoPix = (subtotal *15) / 100
precoPix = subtotal - descontoPix
acrescimoCartao = subtotal * 0.15
precoCartao = subtotal + acrescimoCartao

if escolhido == 1:
    print(f'Pagamento a vista desconto de R${descontoAvista:.2f}, preço final de R$ {precoAvista:.2f}')
elif escolhido == 2:
    print(f'Pagamento com pix, desconto de R${descontoPix:.2f}, preço final de R$ {precoPix:.2f}')
elif escolhido == 3:
    print(f'Pagamento com cartão, acréscimo de R${acrescimoCartao:.2f}, preço final de R$ {precoCartao:.2f}')
else:
    print(f'Opção Inválida!')

