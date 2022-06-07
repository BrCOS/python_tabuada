n_tabuada = int(input('Digite o número para ver sua respectiva tabuada: '))

print('Tabuada de ', n_tabuada)

for i in range(1, 11):
    print(n_tabuada, 'X', i, '=', (n_tabuada * i))