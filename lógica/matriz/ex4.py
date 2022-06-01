listaA = []
listaB = []

for c in range(0,15):
    listaA.append(int(input("Digite um número: ")))
    listaB.append(listaA[c] / 2)

print(listaA, listaB)
