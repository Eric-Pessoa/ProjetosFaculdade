print("Digite 3 números inteiros.")
num1 = int(input(""))
num2 = int(input(""))
num3 = int(input(""))
if(num1 == num2 and num2 == num3):
    print("Você não pode digitar 3 números iguais")
else:
    
    if (num1>num2 and num2>num3):
        print("A ordem crescente é:", num3, ">", num2, ">", num1)
    elif(num1>num3 and num3>num2):
        print("A ordem crescente é:", num2, ">", num3, ">", num1)
    elif(num2>num1 and num1>num3):
        print("A ordem crescente é:", num3, ">", num1, ">", num2)
    elif(num2>num3 and num3>num1):
        print("A ordem crescente é:", num1, ">", num3, ">", num2)
    elif(num3>num2 and num2>num1):
        print("A ordem crescente é:", num1, ">", num2, ">", num3)
    elif(num3>num1 and num1>num2):
        print("A ordem crescente é:", num2, ">", num1, ">", num3)