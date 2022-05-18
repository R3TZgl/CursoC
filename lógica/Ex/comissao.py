vendedor = str(input('Nome do vendedor: ')).strip().title()
vendas = int(input('Total de vendas: '))
com = 0


if vendas <= 250:
    com = 1

elif vendas <= 500:
    com = 1.5

else:
    com = 2
    

print(f'Vendedor: {vendedor} \nTotal de vendas: {vendas} \nComissão: R${vendas * com:.2f}')
