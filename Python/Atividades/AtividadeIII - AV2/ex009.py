'''9 - Faça um programa que permita entrar com números e imprimir o quadrado de cada número
digitado até entrar um número múltiplo de 6 que deverá ter seu quadrado impresso também.'''

i = 0

for i in range(i, 10):
    num = int(input('Digite um número: '))
    
    if num % 6 == 0:
        print(f'\nO número {num} é multiplo de 6')
    print(f'O quadrado de {num} é: {num**2}\n')