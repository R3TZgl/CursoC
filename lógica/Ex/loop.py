from random import randint

contador = 1
r = 0

while contador < 5:
    x = randint(0,10)
    r += x * 3
    print(r)
    contador += 1
