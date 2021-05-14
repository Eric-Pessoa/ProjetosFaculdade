print("Digite um número inteiro, iremos ver se ele é múltiplo de 5 e 10 ao mesmo tempo.")
Num = int(input(""))

Op = Num%10

if(Op == 0):
    print("Sim, ele é múltiplo de 5 e 10.")
else:
    print("Não, ele não é múltiplo de 5 e 10.")

#Só precisei ver se é divisível por 10, pois todo número múltiplo de 10 é também múltiplo de 5, mas nem todo múltiplo
#de 5 é também múltiplo de 10