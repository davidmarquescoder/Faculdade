#1 - Faça um programa que leia 5 números e informe a soma e a média dos números.
i = 0
aux = 0

for i in range(5):
    num = int(input('Digite um número inteiro: '))
    aux += num

print(f'A soma dos números é igual a: {aux}\nA média dos valores é igual a: {aux/5:.1f}')