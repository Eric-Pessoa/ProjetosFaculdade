print("Dê o preço de um produto e seu percentual de desconto, respectivamente")
preco=int(input(""))
desconto=float(input(""))

op = preco - (preco*(desconto/100))
print("seu novo preço é:", op, "e o valor do desconto é:", desconto,"%")