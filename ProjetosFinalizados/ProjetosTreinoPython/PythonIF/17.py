print("Digite o valor da compra de um produto, para saber por quanto você deve vendê-lo.")
Num = int(input(""))
Op = Num * 1.45
Op2 = Num * 1.30

if (Num < 20):
    print(f"Você deve vender o produto por: {Op}.")
else:
    print(f"Você deve vender o produto por: {Op2}.")