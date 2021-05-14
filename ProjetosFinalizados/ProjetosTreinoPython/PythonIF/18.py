print("Menu de opções")
print("1: Somar 2 números.")
print("2: Raiz quadrada de um número.")
Op = input("Digite a opção desejada: ")


if (Op == "1"):
    print("Certo, vamos somar 2 números.")
    Num1 = int(input("Digite o primeiro número que você quer somar: "))
    Num2 = int(input("Digite o segundo número que você quer somar: "))
    Soma = Num1 + Num2
    print("Seu resultado é:", Soma)
elif (Op == "2"):
    print("Certo, vamos tirar a raíz quadrada de um número.")
    raiz = int(input("Digite o número que você deseja saber a raiz: "))
    Op2 = raiz**0.5
    print(f"A raíz do seu número é: {Op2}")