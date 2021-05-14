def chamar_menu():
    menu = ("1. Fazer Inscrição","2. Alterar Inscrição","3. Listar Inscrições","4. Sair")
    print("{:25}".format(" MENU "))
    for item in menu:
        print(f"{item:25}")
        print("-" * 25)
    opcao = input("Escolha: ")
    return opcao

