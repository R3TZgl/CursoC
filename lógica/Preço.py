produto = 'Alface'
preco = 3
imp1 = preco * 2.5 / 100
imp2 = preco * 5 / 100
distribuidor = 0.45

pf = preco + imp1 + imp2 + distribuidor
print(f' O preço final do {produto} é R${pf:.2f}')
