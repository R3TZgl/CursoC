notas = []
aluno = str(input('Nome do aluno: ')).strip().title()

for c in range(0, 3):
    notas.append(int(input(f'Nota {c + 1}: ')))
    
print(f'O aluno {aluno} tirou as seguintes notas: ')

for c in notas:
    print(c)
    