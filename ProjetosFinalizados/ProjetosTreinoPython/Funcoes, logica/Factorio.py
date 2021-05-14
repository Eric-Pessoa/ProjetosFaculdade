

print(f"{'-'*15}Bem vindo{'-'*15}")


def Formula3 ():

    print("PRODUTOS QUE LEVAM 3 MATERIAIS DIFERENTES PARA SEREM FEITOS \n")



    ElementoPrincipal = int(input("Digite a quantidade de material do elemento que você quer usar como base pra fazer o cálculo dos outros. \n"))

    NomeElementoPrincipal = input("Qual o nome desse material? \n")

    ElementoPrincipalMin = int(input("Digite a quantidade desse material que é levada pra fazer 1 item. \n"))

    NomeBagulho2 = input("Digite o nome do segundo material \n")

    Bagulho2 = int(input(f"Digite o valor mínimo de {NomeBagulho2} pra criar esse item. \n"))

    NomeBagulho3 = input("Digite o nome do terceiro material \n")

    Bagulho3 = int(input(f"Digite o valor mínimo de {NomeBagulho3} pra criar esse item. \n"))

    valor1 = ElementoPrincipal/ElementoPrincipalMin

    Bagulho2Resul = Bagulho2*valor1

    Bagulho3Resul = Bagulho3*valor1

    print(f"Quantidade total do material principal ({NomeElementoPrincipal}): {ElementoPrincipal}")
    print(f"Quantidade mínima pra criar 1 item a partir desse material: {ElementoPrincipalMin}")
    print(f"Quantidade de {NomeBagulho2} que será necessário parar criar o mesmo tanto de items que o Elemento principal pode criar: {Bagulho2Resul}")
    print(f"Quantidade de {NomeBagulho3} que será necessário parar criar o mesmo tanto de items que o Elemento principal pode criar: {Bagulho3Resul}")





Formula3()



