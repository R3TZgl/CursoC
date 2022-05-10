while True:
    cliente = str(input('Nome: ')).strip().title()
    if cliente == '':
        print('Erro, digite seu nome!')
    else:
        break
    
arruelas = int(input('Quantas arruelas você comprou? '))
parafusos = int(input('Quantos parafusos você comprou? '))
porcas = int(input('Quantas porcas você comprou? '))

compra = [arruelas, parafusos, porcas]
desconto = [0.7, 0.8, 0.9]
preco = [0.5, 0.8, 0.7]
descontado = 0
total = 0

for n, c in enumerate(compra):

    if c > 1:
        
        valortot = c * preco[n]
        valor = c * desconto[n] * preco[n]
    else:
        valor = c * preco
    total += valortot
    descontado += valor

    if n == 0:
        print(f'Foram compradas {arruelas} arruelas por um valor de R${valor:.2f}.')
    elif n == 1:
        print(f'Foram comprados {parafusos} parafusos por um valor de R${valor:.2f}.')
    elif n == 2:
        print(f'Foram compradas {porcas} porcas por um valor de R${valor:.2f}.')
desc = total - descontado
    
print(f'Cliente: {cliente} \n Valor total: R${descontado:.2f} com um desconto de R${desc:.2f}')
