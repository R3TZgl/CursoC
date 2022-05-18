from random import randint

teto = randint(2000, 3200)
func = randint(0, 6000)

if func >= teto:
    print('Ganhou')

else:
    print('Não ganhou')

print(teto, func)
