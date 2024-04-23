n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

if media==10:
    print(f'A sua nota foi {media}\nAprovado com Glória!')

elif media>=7:
    print(f'A sua nota foi {media}\nAprovado!')
else:
    print(f'A sua nota foi {media}\nReprovado!')
    

    