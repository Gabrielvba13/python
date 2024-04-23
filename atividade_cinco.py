print('Qual operação você deseja realizar?\n[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão')
opcao = int(input('Opção: '))

if opcao==1:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    soma = n1+n2
    print(f'O resultado da soma é: {soma}')

if opcao==2:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    subtracao = n1-n2
    print(f'O resultado da subtracao é: {subtracao}')

if opcao==3:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    multiplicacao = n1*n2
    print(f'O resultado da multiplicação é: {multiplicacao}')

if opcao==4:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    divisao = n1/n2
    print(f'O resultado da divisão é: {divisao}')