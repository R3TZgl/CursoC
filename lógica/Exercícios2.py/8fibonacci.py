numeroUm = 1
numeroDois = 0
total = 0
for c in range(1,14):
    total = numeroDois + numeroUm
    numeroUm = numeroDois
    numeroDois = total
    print(total)