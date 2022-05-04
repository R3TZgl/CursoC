dados = {}
info = ['Marca', 'Km inicial', 'Km final', 'Combústivel', 'Capacidade do tanque']

for c in info:
    if c == info[0]:
        dados[c] = str(input(f'{c}: ')).strip().title()
    else:
        dados[c] = int(input(f'{c}: '))
    
for c in info:
    print(f'{c}: {dados[c]}')

kml = (dados[info[2]] - dados[info[1]]) / dados[info[3]]
print(f'Fez uma média de {kml}km por litros') 
print(f'Sua autonomia é de {kml * dados[info[4]]} km')