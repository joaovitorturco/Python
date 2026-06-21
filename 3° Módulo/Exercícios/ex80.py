#Um programa que vai ler cinco valores numericos, e os cadastre em uma lista ja na posição correta de inserção, sem usar o sort
# No final mostre a lista na tela em ordem, 5, 2, 8, 1, 3

lista = []

for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

print(f'Os valores digitados foram {lista}')