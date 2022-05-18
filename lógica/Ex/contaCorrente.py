from random import randint


nome = str(input('Nome: ')).title().strip()
banco = str(input('Banco: ')).title().strip()
conta = int(input('Número da conta: '))
cheques = randint(0, 800)
credito = randint(0, 2000)
limite = randint(1500, 3000)
saldo = randint(0, 5000)


print(f'Cliente: {nome} \nBanco: {banco} Conta: {conta}')

print(f'Seu saldo atual é de: {saldo + limite + credito - cheques}')
