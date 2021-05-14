positivos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
for i in positivos:
    print(i)

listt = ("oi","novo","macaco","abelololook")

def tupla (lista):
    Maior = 0
    for i in lista:
        if i < Maior:
            continue
        elif i > Maior:
            Maior = i
    print(Maior)


def media (lista):
    com = 0
    count = 0
    for i in lista:
        com += i
        count += 1
    print(com/count)

def pala (lista):
    maior = 0
    for i in lista:
        if len(i) > 0:
            maior = i
    print(maior)







tupla(positivos)
media(positivos)
pala(listt)