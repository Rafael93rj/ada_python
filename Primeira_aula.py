#Inputando informação
"""input('Que linguagem é essa? ')"""

#Variáveis
"""idade = 30
nome = 'Rafael'
altura = 1.70
print(type(idade))
print(type(nome))
print(type(altura))

print(f'Meu nome é {nome},tenho {idade} anos de idade.')"""

#Conversão
idade_dois = '30'
"""print(f'Sua idade daqui a dois anos vai ser {idade_dois + 2}')"""

idade_int = int(idade_dois)
print(f'Sua idade daqui a dois anos vai ser {idade_int + 2}')

#Conversão de input (o input sempre traz como padrão str)
idade_tres = int(input('Digite a sua idade: '))
print(f'A sua idade daqui a 3 anos será {idade_tres + 3}')