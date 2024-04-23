perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
contador = 0

for i in perguntas:
    resposta = input(i)
    if resposta == 's':
        contador += 1

if contador == 5:
    print('Assassino')
elif contador >= 3:
    print('Cúmplice')
elif contador == 2:
    print('Suspeita')
else:
    print('Inocente')
