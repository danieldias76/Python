peso = float(input('Informe seu peso:'))
altura = float(input('Informe sua altura:'))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f'Abaixo do peso')
elif (imc >= 18.5) and (imc <= 24.9):
    print(f'Peso Ideal')
elif (imc >= 24.9) and (imc <= 29.9):
    print(f'Sobrepeso')
else:
    print(f'Obesidade')

print(f'Com peso de {peso} e altura de {altura}, o resultado é {imc:.2f}(faixa de Peso ideal)')


