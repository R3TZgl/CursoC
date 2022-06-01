listaA = []
listaB = []

for c in range(0,20):
    listaA.append(int(input("Digite um número: ")))
    listaB.insert(0 ,listaA[c])

print(listaA, listaB)