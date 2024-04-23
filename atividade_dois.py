'''minuto = int(input('Digite um número: '))
hora = int(input('Digite outro número: '))
dia = int(input('Digite outro número: '))'''

print('~Escolha uma opção para converter em segundos.~\n[1] Converter minutos para segundos\n[2] Converter horas para segundos\n[3] Converter dias para segundos')
opcao = int(input('Digite a opção: '))



if opcao==1:
    minuto = float(input('\nDigite quantos minutos você deseja converter para segundos: '))
    formula = minuto*60
    print(f'{minuto} minutos é igual a {formula} segundos.')

if opcao==2:
    hora = float(input('\nDigite quantas horas você deseja converter para segundos: '))
    formula = hora*3600
    print(f'{hora} horas é igual a {formula} segundos.')

if opcao==3:
    dia = float(input('\nDigite quantos dias você deseja converter para segundos: '))
    formula = (dia)*(24*60*60)
    print(f'{dia} dias é igual a {formula} segundos.')