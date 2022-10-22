#2 - Faça um programa que leia 10 valores e ao final imprima a média aritmética dos  valores lidos.
i = 0
aux = 0

for i in range(10):
    num = int(input('Digite um valor inteiro: '))
    aux += num

print(f'A média dos valores é igual a: {aux/10}')