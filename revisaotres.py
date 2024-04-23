inicio = int(input('Digite o número inicial: '))
final = int(input('Digite o número final: '))
soma=0
for i in range(inicio,final+1):
    if i %2==0:
        print(i)
        soma = soma+i
    print(f'A soma dos números pares são: {soma}')
        