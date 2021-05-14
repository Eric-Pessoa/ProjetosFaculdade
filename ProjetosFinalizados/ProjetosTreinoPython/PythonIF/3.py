print("Digite 3 números inteiros diferentes.")
num1 = int(input(""))
num2 = int(input(""))
num3 = int(input(""))

if (num1>num2 and num2>num3):
    print("A ordem decrescente é:", num1, ">", num2, ">", num3)
elif(num1>num3 and num3>num2):
    print("A ordem decrescente é:", num1, ">", num3, ">", num2)
elif(num2>num1 and num1>num3):
    print("A ordem decrescente é:", num2, ">", num1, ">", num3)
elif(num2>num3 and num3>num1):
    print("A ordem decrescente é:", num2, ">", num3, ">", num1)
elif(num3>num2 and num2>num1):
    print("A ordem decrescente é:", num3, ">", num2, ">", num1)
elif(num3>num1 and num3>num1):
    print("A ordem decrescente é:", num3, ">", num1, ">", num2)