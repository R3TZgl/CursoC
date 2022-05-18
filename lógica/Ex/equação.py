from math import sqrt
from random import randint
from random import choice

sinaisb = ''
sinaisc = ''
a = 0

while a == 0:
    a = randint(-10, 10)
b = randint(-10, 10)
c = randint(-10, 10)

if b >= 0:
    sinaisb = '+'

if c >= 0:
    sinaisc = '+'

print(f'{a}x² {sinaisb} {b}x {sinaisc} {c} = 0')

delta = b ** 2 - 4 * a * c

if delta >= 0:
    bhaskarap = (- b + sqrt(delta)) / (2 * a)
    bhaskaran = (- b  - sqrt(delta)) / (2 * a)
    print(f'x´ = {bhaskarap:.2f}, x´´ = {bhaskaran:.2f} ')
else:
    print('As raízes são imaginárias.')
    