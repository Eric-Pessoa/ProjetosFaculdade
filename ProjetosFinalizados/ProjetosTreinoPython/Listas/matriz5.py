lista = []

count = 0
for n in range(5):
    ele1 = int(input("Informe um número: \n"))
    ele2 = int(input("Informe outro número: \n"))
    ele3 = int(input("Informe outro número: \n"))
    ele4 = int(input("Informe outro número: \n"))
    listaresult1 = [ele1,ele2,ele3,ele4]
    lista.append(listaresult1)

for x in lista:
    print(f"{x}")
