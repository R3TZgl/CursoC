semana = 10000
meta = 9800
total = 0
perda = 0.95

print(f'Sua meta é de {meta} por semana.')

for c in range(0,4):
    sit = str(input(f'Houve queda de energia na semana {c+1}?  ')).strip().lower()[0]
    
    if 's' in sit:
        total += semana * perda
    else:
        total += semana
    if total < meta * (c + 1):
        print('Você não atingiu a meta.')

print(f'Você totalizou {total} peças este mês.') 