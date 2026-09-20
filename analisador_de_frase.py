print('=== ANALISADOR DE NOME / FRASE ===\n')

n1 = input('Digite um nome ou frase: ').strip()

n2 = n1.replace(' ','')

palavras = n1.split()

print(f'Analisando: {n1}\n')

print(f'O texto possui {len(n1)} caracteres com espaço')

print(f'O texto possui {len(n2)} caracteres sem espaço')

print(f'Quantidade de palavras: {len(palavras)}')

print(f'A primeira palavra: {palavras[0]}')

print(f'A ultima palavra: {palavras[-1]}')

letra = input('Digite uma letra:').strip()

if letra == '':
    print('Campo Vazio,caractere inválido')
else:
    print(f'A letra: ({letra}) aparece {n1.lower().count(letra.lower())} vezes ')

