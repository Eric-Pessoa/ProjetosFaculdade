from funcoes import *

opcao = chamar_menu()
alunos = []
nomesAluno = []

while opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
    print("Opção inválida! Digite novamente!\n")
    opcao = chamar_menu()

while opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
    if opcao == "1":
        alunos = inscricao()
        opcao = chamar_menu()

    elif opcao == "2":
        if len(alunos) == 0:
            print("Ainda não há inscritos!")
            opcao = chamar_menu()
        else:
            alteracao_dados = str(input("\nEscolha o dado para alteração:\n1- CPF\n2- Matrícula\nEscolha: "))
            while alteracao_dados != "1" and alteracao_dados != "2":
                print("Escolha o número de acordo com as opções apresentadas. Tente novamente.")
                alteracao_dados = str(input("Escolha o dado para alteração:\n1- CPF\n2- Matrícula\nEscolha: "))
            if alteracao_dados == "1":
                cpfAlunos = alterar_inscricao_cpf(alunos[1])
            else:
                matAlunos = alterar_inscricao_mat(alunos[0])
            opcao = chamar_menu()

    elif opcao == "3":
        listar_inscricoes()
        opcao = chamar_menu()
    else:
        print("\n---- FIM DO PROGRAMA ----")
        exit()
