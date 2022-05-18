nome = str(input('Nome: ')).strip().title()
descricao = str(input('Descrição: ')).strip().title()
frequencia = int(input('Frequência: '))
mediamin = int(input('Média mínima para aprovação: '))

print(f'Nome: {nome}')
print(f'Descrição: {descricao}')
print(f'Frequência: {frequencia}%')
print(f'Média mínima: {mediamin}')