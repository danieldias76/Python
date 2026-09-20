a = float(input('Informe o lado A:'))
b = float(input('Informe o lado B:'))
c = float(input('Informe o lado C:'))

if a + b > c and a + c > b and b + c > a:
    print(f'Pode ser um trianqulo {a+b+c}')
else:
    print(f'Nâo pode ser um trianqulo! {a+b+c}')