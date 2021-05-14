print("Pensei num número, tente adivinhar qual é.")
Segredo = 56
Num = int(input(""))
Cont = 1

while(Num!=Segredo):
    if (Num > Segredo):
        print("Errou por mais. Tente de novo.")
        Num = int(input(""))
        Cont += 1
    elif (Num < Segredo):
        print("Errou por menos. Tente de novo")
        Num = int(input(""))
        Cont += 1
print("Tu acertou, parabéns otario. Levou", Cont, "tentativas.")
