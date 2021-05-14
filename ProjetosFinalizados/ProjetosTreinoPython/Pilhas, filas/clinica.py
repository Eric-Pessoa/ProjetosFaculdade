from collections import deque

ContadorSenha = 0
ContadorIdoso = 0
filaNormal = deque([])
filaIdoso = []
Primeira_vez = True

#Não tá certo, mas foi quase, um dia eu volto aqui e resolvo


def inicio():
    print("Bom dia, selecione uma opção: \n")
    print(" 1 - Imprimir nova senha \n")
    print(" 2 - Imprimir nova senha (prioridade) \n")
    print(" 3 - Relatório: mostrar fila de atendimento \n")
    print(" 4 - Atender paciente \n")
    print(" 5 - sair \n")

    return int(input("Digite a opção que você quer: "))

def sair():
    print("Saindo...")



def ImprimirNovaSenha(ContadorSenha):
    ContadorSenha += 1
    filaNormal.append(ContadorSenha)
    return ContadorSenha

def ImprimirSenhaPrioridade(ContadorSenha, ContadorIdoso):
    ContadorSenha += 1
    ContadorIdoso += 1
    print(filaIdoso)
    filaIdoso.append(ContadorSenha)
    print(filaIdoso)
    return ContadorSenha, ContadorIdoso


def MostrarRelatorio():
    print("\nA fila de atendimento é, da esquerda pra direita: ")
    for n in filaNormal:
        print(n, end= ' ')
    print("\n")

def AtenderPaciente():
    if(filaNormal[0] == filaIdoso):
        filaNormal.popleft()
    print(f"Paciente com a senha {filaNormal[0]} foi tratado com sucesso.")



while True:
    opcao = inicio()

    if(opcao == 1):
        ContadorSenha = ImprimirNovaSenha(ContadorSenha)
        print(f"Cadastrado com sucesso! Sua senha é: {ContadorSenha}")
        print(filaNormal)

    if(opcao == 2):
        ContadorSenha,ContadorIdoso = ImprimirSenhaPrioridade(ContadorSenha,ContadorIdoso)
        print(f"Boa idoso, mandou bem. Sua senha é: {ContadorSenha}")
        if(Primeira_vez):
            filaNormal.appendleft(filaIdoso)
            Primeira_vez = False
        else:
            filaNormal.popleft()
            filaNormal.appendleft(filaIdoso)
        print(filaNormal)

    if(opcao == 3):
        MostrarRelatorio()

    if(opcao == 4):
        AtenderPaciente()

    if(opcao == 5):
        sair()
        break


