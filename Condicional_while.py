#Condicional While

number_user = int(input('Digite um número: '))

while number_user != 5:
    print('Você errou, tente novamente!')
    number_user = int(input('Digite um número: '))
else:
    print('Parabéns, você acertou!')


#Contador

contador = 0

while contador < 10:
    print(contador)
    contador = contador + 1
