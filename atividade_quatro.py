print('Olá, seja bem-vindo(a) ao sistema de conversão de temperatura.\n[1] - Converter de Celsius para Fahrenheit\n[2] Converter Fahrenheit para Celsius')
opcao = int(input('Digite sua opção: '))

if opcao==1:
    graus = float(input('Digite quantos Graus Celsius você deseja converter para Fahrenheit: '))
    fahrenheit = (graus * 9/5) + 32
    print(f'A temperatura em Fahrenheit é: {fahrenheit}')

if opcao==2:
    fahrenheit = float(input('Digite quantos Fahrenheit você deseja converter para Graus Celsius: '))
    graus = (fahrenheit - 32) * 5/9
    print(f'A temperatura em Fahrenheit é: {graus}')