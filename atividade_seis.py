# Pergunta para a criança o valor da hora de trabalho e quantas horas trabalhou
valor_hora = float(input("Quanto vale 1 hora do seu trabalho? (em reais) "))
horas_trabalhadas = float(input("Quantas horas você trabalhou este mês? "))

# Calcula o salário bruto (valor da hora * quantidade de horas trabalhadas)
salario_bruto = valor_hora * horas_trabalhadas

# Calcula o desconto do INSS (10% do salário bruto)
inss_desconto = salario_bruto * 0.10

# Verifica em qual faixa de desconto de IR o salário bruto se encaixa e calcula o desconto correspondente
if salario_bruto <= 900:
    ir_desconto = 0
elif salario_bruto <= 1500:
    ir_desconto = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir_desconto = salario_bruto * 0.10
else:
    ir_desconto = salario_bruto * 0.20

# Calcula o FGTS (11% do salário bruto)
fgts = salario_bruto * 0.11

# Calcula o total de descontos (IR + INSS)
total_descontos = ir_desconto + inss_desconto

# Calcula o salário líquido (salário bruto - total de descontos)
salario_liquido = salario_bruto - total_descontos

# Mostra para a criança todas as informações calculadas
print("Seu salário bruto é: R$ {:.2f}".format(salario_bruto))
print("Você terá um desconto de R$ {:.2f} de IR e R$ {:.2f} de INSS".format(ir_desconto, inss_desconto))
print("O FGTS depositado será de R$ {:.2f}".format(fgts))
print("Seu salário líquido, depois dos descontos, será de R$ {:.2f}".format(salario_liquido))
