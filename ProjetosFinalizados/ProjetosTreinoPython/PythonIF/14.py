print("Digite o valor de 3 lados de um triângulo e veja que tipo e triângulo ele formaria.")
lado1 =(int(input("")))
lado2 =(int(input("")))
lado3 =(int(input("")))

if (lado1 == lado2 and lado2 == lado3):
    print("É um triângulo equilátero")
elif (lado1 == lado2 or lado2 == lado3 or lado3 == lado1):
    print("É um triângulo isósceles.")
else:
    print("você tem um triângulo escaleno.")