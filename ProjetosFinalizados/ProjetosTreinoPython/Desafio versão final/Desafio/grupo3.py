import re

def validar_cpf(cpf):
    cpf = ''.join(re.findall('\d', str(cpf)))
    novo = cpf[:9]

    # digito 1
    l1 = []
    for i, v in reversed(list(enumerate(reversed(novo)))):
        l1.append((i + 2) * int(v))
    resto = sum(l1) % 11

    if resto < 2:
        f = 0
    else:
        f = 11 - resto
    novo += str(f)

    # digito 2
    l2 = []
    for i, v in reversed(list(enumerate(reversed(novo)))):
        l2.append((i + 2) * int(v))
    resto = sum(l2) % 11

    if resto < 2:
        f = 0
    else:
        f = 11 - resto
    novo += str(f)

    if novo == '00000000000' or novo == '11111111111' or novo == '22222222222' or novo == '33333333333' or novo == '44444444444' or novo == '55555555555' or novo == '66666666666' or novo == '77777777777' or novo == '88888888888' or novo == '99999999999':
        print(" CPF inválido. Digite novamente")
    else:
        if cpf == novo:
            validade = True

        else:
            validade = False

    return validade




#-----------TESTE MENU----------------
# cont =1
# while cont > 0:
#     print("Menu")
#     print("1. Fazer inscrição.")
#     print("2. Alterar inscrição.")
#     print("3. Listar inscrição.")
#     print("4. Sair.")
#     cont += 1
#     opcao = int(input("****Digite a opção desejada!****: "))
#     "\n"
#     if (opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4):
#         opcao = int(input("****Digite a opção desejada!****: "))
#
#     if (opcao ==1):
#         nome_aluno = input("Nome do aluno: ")
#         cpf = input("CPF: ")
#         print(validar_cpf(cpf))

