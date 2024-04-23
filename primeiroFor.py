'''nota = int(input('Digite um número de 0 a 10: '))

while nota > 10 or nota < 0:
    nota = int(input("Informe um valor válido: "))
    
    ---------------------------
nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

while senha==nome:
    print('Não pode usar a senha como nome de usuário.')
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    ----------------------------
    
    ------------------------------
    
n1 = int(input('Digite o um número: '))
n2 = int(input('Digite outro número: '))

for i in range(n1+1,n2):
    print(i)'''    
    
def soma (n1,n2,n3):
    res = n1+n2+n3
    return res

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

resultado = soma(n1,n2,n3)

print (f'O resultado da soma é: {resultado}')


