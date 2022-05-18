import math

hora = float(input("Quanto você ganha por hora? "))
tempo = float(input("Quantas horas você trabalha por semana? "))
bruto = hora * (4 * tempo)
inss = 0


if bruto < 1212.00:
    inss = bruto * (7.5 / 100)

elif 2427.35 < bruto > 1212.01:
    inss = bruto * (9 / 100)

elif bruto < 3641.03:
    inss = bruto * (12 / 100)

elif bruto < 7087.22:
    inss = bruto * (14 / 100)

else:
    inss = 7087.22 *(14 / 100)
    

salario = bruto - inss

print(salario)


