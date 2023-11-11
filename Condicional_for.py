#Condicional For

"""for variavel in range(10):
    print(variavel)"""

"""for variavel in range(1, 11, 2):
    print(variavel)"""

soma = 0

for i in range(1,4):
    nota = float(input(f'Informe a sua nota {i}: '))

    soma = soma + nota

print(round(soma / 3))