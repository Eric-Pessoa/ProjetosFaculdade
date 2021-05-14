lista = []

count = 0
for n in range(8):
    ele1 = int(input("Informe um número: \n"))
    ele2 = int(input("Informe outro número: \n"))
    ele3 = int(input("Informe outro número: \n"))
    ele4 = int(input("Informe outro número: \n"))
    ele5 = int(input("Informe outro número: \n"))
    ele6 = int(input("Informe outro número: \n"))
    ele7 = int(input("Informe outro número: \n"))
    ele8 = int(input("Informe outro número: \n"))

    if (count == 0):
        NumEspecial1 = ele1
        listaResult1 = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8]
        lista.append(listaResult1)
        count += 1

    elif (count == 1):
        NumEspecial2 = ele2
        listaResult1 = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8]
        lista.append(listaResult1)
        count += 1


    elif (count == 2):
        NumEspecial3 = ele3
        listaResult1 = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8]
        lista.append(listaResult1)
        count += 1


    elif (count == 3):
        NumEspecial4 = ele4
        listaResult1 = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8]
        lista.append(listaResult1)
        count += 1


    elif (count == 4):
        NumEspecial5 = ele5
        listaResult1 = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8]
        lista.append(listaResult1)
        count += 1

    elif (count == 5):
        NumEspecial6 = ele6
        listaResult1 = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8]
        lista.append(listaResult1)
        count += 1

    elif (count == 6):
        NumEspecial7 = ele7
        listaResult1 = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8]
        lista.append(listaResult1)
        count += 1

    elif (count == 7):
        NumEspecial8 = ele8
        listaResult1 = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8]
        lista.append(listaResult1)
        count += 1

var = NumEspecial1 + NumEspecial2 + NumEspecial3 + NumEspecial4 + NumEspecial5 + NumEspecial6+ NumEspecial7 + NumEspecial8

print(f"A soma dos elementos da diagonal principal é: {var}")

print(lista)