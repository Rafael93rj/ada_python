#Selecionando um item da lista

salario1 = float(input('Digite o primeiro salário: '))
salario2 = float(input('Digite o segundo salário: '))
salario3 = float(input('Digite o terceiro salário: '))

renda_total = [salario1, salario2, salario3]

print(f'A média salarial da família é: {round(sum(renda_total)/3)}')

