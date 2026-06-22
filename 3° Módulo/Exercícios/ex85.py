valores = [[], []]

for c in range(3):
    n = int(input('Digite um valor: '))

    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

valores[0].sort()
valores[1].sort()

print('-'*30)

if valores[0]:
    print(f'Os valores pares são (em ordem crescente):')
    for valor in valores[0]:
        print(valor)
else:
    print('Não há valores pares')

if valores[1]:
    print('Os valores impares são (em ordem crescente):')
    for valor in valores[1]:
        print(valor)
else:
    print('Não há valores impares')