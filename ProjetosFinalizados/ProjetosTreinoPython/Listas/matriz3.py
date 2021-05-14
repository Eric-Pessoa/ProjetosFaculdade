lista = []

count = 0
for n in range(5):
    ele1 = int(input("Informe um número: \n"))
    ele2 = int(input("Informe outro número: \n"))
    ele3 = int(input("Informe outro número: \n"))
    ele4 = int(input("Informe outro número: \n"))
    ele5 = int(input("Informe outro número: \n"))

    if (count == 0):
        NumEspecial1 = ele5
        listaResult1 = [ele1, ele2, ele3, ele4, ele5]
        lista.append(listaResult1)
        count += 1

    elif (count == 1):
        NumEspecial2 = ele4
        listaResult1 = [ele1, ele2, ele3, ele4, ele5]
        lista.append(listaResult1)
        count += 1


    elif (count == 2):
        NumEspecial3 = ele3
        listaResult1 = [ele1, ele2, ele3, ele4, ele5]
        lista.append(listaResult1)
        count += 1


    elif (count == 3):
        NumEspecial4 = ele2
        listaResult1 = [ele1, ele2, ele3, ele4, ele5]
        lista.append(listaResult1)
        count += 1


    elif (count == 4):
        NumEspecial5 = ele1
        listaResult1 = [ele1, ele2, ele3, ele4, ele5]
        lista.append(listaResult1)
        count += 1

var = NumEspecial5 + NumEspecial4 + NumEspecial3 + NumEspecial2 + NumEspecial1

print(f"A soma dos elementos da diagonal secundária é: {var}")

print(lista)
