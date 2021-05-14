# 7 elementos com 2 valores cada.

lista = []

for n in range(2):
    ele1 = int(input("Informe um número: \n"))
    ele2 = int(input("Informe outro número: \n"))
    lista2 = [ele1, ele2]
    lista.append(lista2)


for n in lista:
    for y in n:
        if y >= 10 and y <= 20:
            print(f"Números maiores que 10 e menores que 20:{y}")








    #for element in n:
       # if(element >= 10 or element <= 20):
           # print(element)


