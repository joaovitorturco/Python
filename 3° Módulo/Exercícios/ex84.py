#um programa vai ler varios dados (nome e peso) de varias pessoas, e vai mostrar
#a) o total de pessoas cadastradas
#b) as pessoas mais pesadas
#c) as pessoas mais leves


dados = list()
pessoas = list()
pessoas_pesadas = list()
pessoas_leves = list()
quantidadePessoas = 0


while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if dados[1] >= 100:
        pessoas_pesadas.append(dados[0])
    elif dados[1] <= 70:
        pessoas_leves.append(dados[0])


    quantidadePessoas += 1
    pessoas.append(dados[:])
    dados.clear()
    res = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if res == 'n':
        break

print('-'*30)
print(f'Quantidade de pessoas cadastradas: {quantidadePessoas}')

if pessoas_pesadas:
    print('Pessoas com o peso maior ou igual a 100KG')
    for p in pessoas_pesadas:
        print(f'{p}')
    print('')

if pessoas_leves:
    print('Pessoas com o peso menor ou igual a 70KG:')
    for p in pessoas_leves:
        print(f'{p}')
    print('')





# 70 kg - pessoas leves
# 100 kg pessoas pesadas