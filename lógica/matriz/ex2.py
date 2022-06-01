listaA = []
listaC = []

for c in range(0,2):
    listaA = []
    for c in range(0,2):
        listaA.append(int(input("Digite um número: ")))
        listaC.append(listaA[c])

print(listaC)