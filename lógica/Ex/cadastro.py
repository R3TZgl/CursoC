dados = {}
info = ['Nome', 'Endereço', 'Cidade', 'UF', 'CEP', 'Telefone', 'CPF',
        'RG', 'Data De Nascimento', 'Grau De Escolaridade', 'Curso']
for c in info:
    while True:
        dados[c] = str(input(f'{c}: ')).strip().title()
        if dados[c] != '':
            break
        else:
            print('Erro, insira os dados corretamente.')

for c in info:
    print(f'{c}: {dados[c]}')

    dados["Nome"] = "sim"
    print(dados["Nome"][2])