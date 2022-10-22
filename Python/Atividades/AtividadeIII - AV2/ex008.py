'''8 - Faça um programa  que leia 10 números positivos e imprima o quadrado de cada número.
Para cada entrada de dados deverá haver um trecho de validação para que um número negativo
não seja aceito pelo programa.'''

i = 0

for i in range(i, 10):
    while(True):
        try:
            num = int(input('Digite um número inteiro positivo: '))
            if num < 0:
                print('\nVocê só pode inserir valores POSITIVOS!!!\n')
                continue
            else:
                print(f'{num**2}\n')
            break
        except:
            print('\nDigite apenas números inteiros e positivos!!\n')