'''3 - Faça um programa que leia "n" valores. O programa deve inicialmente solicitar ao usuário que informe
a quantidade desejada de valores a ser informada, depois ler os "n" valores e ao final imprimir a média 
aritmética dos valores lidos.'''
i = 0
aux = 0

while(True):
    try:
        x = int(input('Digite quantos valores deseja inserir: '))
        break
    except:
        print('\nDigite apenas números inteiros!!\nNão valem letras nem caracteres e nem números reais!!!!\n')

for i in range(x):
    valores = int(input('Digite um valor inteiro: '))
    aux += valores

print(f'A média dos valores é igual a: {aux/x}')