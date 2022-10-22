#7 - Faça um programa que realize a soma de todos os valores inteiros de 1 a n, sendo que n deve ser informado pelo usuário.

n = int(input('Digite o alcance do laço: '))
i = 1
aux = 0

for i in range(i, n + 1):
    aux += i

print(aux)