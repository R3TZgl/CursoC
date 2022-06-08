alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q","r","s","T","u","v","w","x","y","z"]
letrasI = {}
nome = []
for c in range(0,3):
    nome.append(str(input("Digite seu nome:").strip().title()))
for c in nome:
    print(c)


for c in alfabeto:
    for i in nome:
        if i[0].lower() == c:
            if f"{c}" in letrasI:
                letrasI[f"{c}"].append(i)
            else:
                letrasI[f"{c}"] = [i]
                