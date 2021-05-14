

lista = []

for n in range(2):
    ele1 = int(input("Informe um número: \n"))
    ele2 = int(input("Informe outro número: \n"))
#    ele3 = int(input("Informe outro número: \n"))
#    ele4 = int(input("Informe outro número: \n"))
    listaresult1 = [ele1,ele2]
    lista.append(listaresult1)






def QuadOuN(lista):
    countlinha = 0
    countColuna = 0
    ListaColuna = []

    for n in lista:
        countlinha += 1
        for y in n:
            countColuna += 1
            ListaColuna.append(y)

    if (len(ListaColuna) / countlinha == countlinha):
        print("É matriz quadrada")
    else:
        print("Não é matriz quadrada")


QuadOuN(lista)