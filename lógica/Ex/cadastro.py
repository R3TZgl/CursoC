dados = {}
info = ['Nome', 'Endereço', 'Cidade', 'UF', 'CEP', 'Telefone', 'CPF',
        'RG', 'Data De Nascimento', 'Grau De Escolaridade', 'Curso']
for c in info:
    if c == info[4] or c == info[5] or c == info[6] or c == info[7] or c == info[8]:
        dados[c] = int(input(f'{c}: '))

    else:
        while True:
            dados[c] = str(input(f'{c}: ')).strip().title()
            if dados[c] != '':
                break
            else:
                print('Erro, insira os dados corretamente.')

for c in info:
    print(f'{c}: {dados[c]}')