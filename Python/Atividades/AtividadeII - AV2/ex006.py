import  os
os.system('cls')
print('=======Passagens=======')
print('[1] Região norte - ida R$ 500; ida e volta R$ 900\n[2] Região nordeste - ida R$ 350; ida e volta R$ 650')
print('[3] Região centro-oeste - ida R$ 350; ida e volta R$ 600\n[4] Região sul - ida R$ 300; ida e volta R$ 550')

destino = input('Informe o destino da sua viagem: ')

if destino == '1':
    while(True):
        os.system('cls')
        print('[1] - Apenas ida\n[2] - Ida e volta')
        opcao = input('Qual a opção desejada? ')
        if opcao == '1':
            print(f'O valor da passagem é igual a: R$ 500 reais')
            break
        elif opcao == '2':
            print(f'O valor das passagens é igual a: R$ 900 reais')
            break
        else:
            print('Digite uma opção válida!! (1 ou 2)')
            os.system('pause')
            continue
if destino == '2':
    while(True):
        os.system('cls')
        print('[1] - Apenas ida\n[2] - Ida e volta')
        opcao = input('Qual a opção desejada? ')
        if opcao == '1':
            print(f'O valor da passagem é igual a: R$ 350 reais')
            break
        elif opcao == '2':
            print(f'O valor das passagens é igual a: R$ 650 reais')
            break
        else:
            print('Digite uma opção válida!! (1 ou 2)')
            os.system('pause')
            continue