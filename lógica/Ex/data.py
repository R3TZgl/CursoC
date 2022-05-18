dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

print(f'{dia}/{mes}/{ano}')

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro' ]

print(f'Joinville, {dia} de {meses[mes+1]} de {ano}')