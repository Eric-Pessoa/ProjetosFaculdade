print("Qual termo da posição fibonacci você quer saber? digite um número")
Num = int(input(""))


Num3 = 2
Num4 = 0
cont = 2


if(Num==1 or Num==2):
    print("1")


while(Num!= cont):
    print(Num3)
    Num3 = (Num3-1)+(Num3-2)
    cont = cont + 1

