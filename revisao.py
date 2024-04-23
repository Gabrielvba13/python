def calculoFatorial(numFat):
        calculo = 1
        for i in range(1,numFat+1):
             calculo = calculo*i
        return calculo
        

num = int(input('Qual número voce deseja fatoria?\n'))
resultado = calculoFatorial(num)
print(resultado)