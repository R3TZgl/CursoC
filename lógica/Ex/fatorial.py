x = int(input('Número: '))

for c in range(x,0,-1):
    if c == x:
        fat = x
    else:
        fat = fat * c
print(fat)