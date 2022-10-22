'''10 - Uma transportadora utiliza caminhões que suportam até 10 toneladas de peso, as caixas transportadas tem tamanho fixo e o caminhão
comporta no máximo 200 volumes, assim, esta transportadora precisa controlar a quantidade e o peso dos volumes para acomodar nos caminhões.
Faça um programa que leia n caixas e seu peso, ao final, o programa deve imprimir a quantidade de volumes, o peso total dos volumes e o 
peso médio dos volumes.'''
i = 1
peso_t = 0

while(True):
    try:
        ncaixas = int(input('Digite com quantas caixas deseja carregar o caminhão: '))
        print('\n')
        break
    except:
        print('\nDigite apenas valores INTEIROS!\n')

for i in range(i, ncaixas + 1):
    while(True):
        try:
            peso_c = float(input(f'Digite o peso da caixa Nº {i} (Em KG): '))
            peso_t += peso_c
            break
        except:
            print('\nDigite apenas valores REAIS! (Floats)\n')

print(f'\nQuantidade de volumes: {ncaixas}\nPeso total dos volumes: {peso_t:.1f}KG\nPeso médio dos volumes: {peso_t/ncaixas:.1f}KG')

if peso_t > 10000:
    print('\nO caminhão ultrapassou o valor suportado de 10 toneladas, não está apto a seguir viagem, reduza o peso total!')
else:
    print('\nO caminhão está apto a seguir viagem, peso total da carga é inferior ou igual a 10 toneladas')