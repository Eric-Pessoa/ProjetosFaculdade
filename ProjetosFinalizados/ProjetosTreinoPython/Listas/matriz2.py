

lista = []
lista2 = []
Lista3 = []

for n in range(2):
    ele1 = int(input("Informe um número: \n"))
    ele2 = int(input("Informe outro número: \n"))
    listaResult1 = [ele1, ele2]
    lista.append(listaResult1)


for n in range(2):
    ele1 = int(input("Informe um número: \n"))
    ele2 = int(input("Informe outro número: \n"))
    listaResult2 = [ele1, ele2]
    lista2.append(listaResult2)


print(lista,lista2)

for j,m in lista,lista2:
    Lista3.append(j + m)

print(Lista3)

linha = []
linha2 = []

for n in Lista3:
    if(len(linha) < 4):
        for j in n:
            linha.append(j)
    else:
        for j in n:
            linha2.append(j)


print(linha)
print(linha2)

listafinal = []


for n in range(len(linha)):
    var = linha[n] + linha2[n]
    listafinal.append(var)



print(listafinal)
