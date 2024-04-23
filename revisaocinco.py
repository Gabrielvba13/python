pTermo = int(input('Digite o primeiro termo:'))
qTermo = int(input('Digite a quantidade de termos:'))
rTermo = int(input('Digite a razão dos termos: '))

fTermo = pTermo + qTermo
calculo = pTermo
print(pTermo)
soma = 0
for i in range(pTermo,fTermo+1):
    calculo = calculo+rTermo
    soma = soma + calculo
    print(calculo)
print(f'As somas dos números são: {soma}')
