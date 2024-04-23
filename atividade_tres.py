valor = float(input('Digite o valor do apartamento que você deseja comprar: '))
salario = float(input('Digite seu sálario: '))
anos = int(input("Digite a quantidade de anos a pagar: "))


meses = anos * 12
prestacao = valor / meses
prestacao_salario = salario * 0.4

if prestacao<=prestacao_salario:
    print(f'Empréstimo aprovado! O valor da prestação mensalmente é: {prestacao}')
else:
    print("Empréstimo negado! A prestação mensal excede 40% do salário.")