# o programa vai ler varios numeros, joga los em uma lista, separar em mais duas listas os pares e impares, e depois mostrar
numeros = []
pares = []
impares = []

while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = input('Deseja continuar? [S/N]: ').strip().lower()
    if resp == 'n':
        break

pares.sort()
impares.sort()

print('-' * 30)
print('Os valores digitados foram: ',end='')
for n in numeros:
    print(f'{n}', end=' ')

print('\nOs valores pares foram: ',end='')
for p in pares:
    print(f'{p}', end=' ')

print('\nOs valores impares foram: ', end='')
for i in impares:
    print(i, end=' ')