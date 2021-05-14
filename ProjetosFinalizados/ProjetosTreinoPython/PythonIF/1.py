print("Informe as 3 notas do seu estudante. a do trabalho de laboratório, a avaliação semestral e o exame final, respectivamente.")
Lab = float(input(""))
Sem = float(input(""))
final = float(input(""))

Peso2 = Lab*0.2
Peso3 = Sem*0.3
Peso5 = final*0.5

NotaFinal = (Peso2+Peso3+Peso5)

if (NotaFinal < 0 or NotaFinal > 10):
    print ("Você digitou algum número inválido")
else:
    print("Sua média ponderada foi:", NotaFinal)
    if (NotaFinal >= 8 and NotaFinal <= 10):
        print ("Conceito A")
    elif (NotaFinal >=7 and NotaFinal <=7.9):
        print ("Conceito b")
    elif (NotaFinal >=6 and NotaFinal <=6.9):
        print ("Conceito C")
    elif (NotaFinal >=5 and NotaFinal <=5.9):
        print ("Conceito D")
    elif (NotaFinal >=0 and NotaFinal <=4.9):
        print ("Conceito E")