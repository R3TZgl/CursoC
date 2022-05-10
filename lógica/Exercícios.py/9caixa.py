valor = int(input('Qual o valor de troco? R$'))

notas = [100,10,1]
troco = [0,0,0]

for n,c in enumerate(notas):
    if valor >= c :
        while valor >= c:
            troco[n] += 1
            valor -= c

print(f'Serão entregues {troco[0]} notas de R${notas[0]:.2f}, {troco[1]} notas de R${notas[1]:.2f} e {troco[2]} notas de R${notas[2]:.2f}')