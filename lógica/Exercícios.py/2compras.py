lista = {}
itens = ['Café', 'Leite', 'Banana']
valores = [17, 5, 10]
total = 0

print('Café | R$17,00 \nLeite | R$5,00 \nBanana | R$10,00')

for n, c in enumerate(itens):
    unidade = 'quilos'

    if c == itens[1]:
        unidade = 'litros'
    print(valores[n])
    lista[c] = [input(f'Quantos {unidade} você comprou de {c}? '), valores[n]]
    total += (lista[c] * valores[n])

for c in itens:
    print(f'{c}: R${lista[c]:.2f}')

print(total)

def 

for i in range(0,10):
    print(i)
