#if else em uma linha
total = 2
numero = 5 if total == 2 else 6

from random import randint
numero = randint(1,10)
print(numero) if numero < 6 else print('Muito grande.')




#List Comprehation
cachorro = ['dog','Hotwailler', 'Pinscher']

lista = [x for x in cachorro if len(x) > 6]

