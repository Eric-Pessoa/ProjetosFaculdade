from defs import validaSenha
from defs import validaCod

listaCod = [] #Lista do codigo do produto
listaDescricao = [] # Lista da Descricao do produto
listaQuant = [] # Lista da quantidade de produtos
contadorErrouSenha = 0 # Permite que o usuário tenha 3 chances de digitação da senha
opcao = 0
contDigitacaoSenha = 0 #contDigitacaoSenha foi criada para permitir que o usuário digite a senha correta apenas uma vez no sistema (conforme regra "b" do topico Considerações)

def cadastraProduto():
    codProd = int(input("Digite o código do produto: "))
    descricaoProd = input("Digite a descrição do produto: ")
    quantProd = int(input("Digite a quantidade de produto em estoques: "))

    if quantProd <= 0:
        print("PRODUTO NÃO PODE SER COMPRADO POIS É MENOR OU IGUAL A ZERO")

    else: 
        #If a seguir valida se o valor digitado pelo usuário já está contido na lista
        for n in listaCod:
            if n==codProd:
                print("ESSE CÓDIGO DE PRODUTO JÁ EXISTE NO SISTEMA!!")
                break
        #Grava os novos valores em sua respectivas listas 
        if(codProd not in listaCod):
            listaCod.append(codProd)
            listaDescricao.append(descricaoProd)
            listaQuant.append(quantProd)
            print("PRODUTO CADASTRADO COM SUCESSO!!")

def alteraProduto():
    retornaN = validaSenha(listaCod, listaDescricao, listaQuant, contadorErrouSenha, contDigitacaoSenha)
    #O if a seguir serve para impedir a continuidade do codigo caso os retornos (codNaoCadastrado ou fimSenha) sejam informados pela funcao validaSenha
    if ((retornaN != "codNaoCadastrado") and (retornaN != "fimSenha")):
        print("1 - Descrição\n2 - Quantidade")
        opcaoParaAlteracao = int(input("Digite umas das opções a cima que deseja alterar: "))
        if opcaoParaAlteracao==1:
            nova_Descrição = input("Digite a nova descrição: ")
            listaDescricao.insert(retornaN,nova_Descrição)
            del listaDescricao[retornaN+1]
            print("ALTERAÇÃO REALIZADA COM SUCESSO")
        elif (opcaoParaAlteracao ==2):
            nova_Quant = int(input("Digite a nova quantidade em estoque: "))
            if nova_Quant <= 0:
                print("PRODUTO NÃO PODE SER CADASTRADO POIS É MENOR OU IGUAL A ZERO")
            else:
                # del listaQuant[retornaN]
                listaQuant.insert(retornaN,nova_Quant)
                del listaQuant[retornaN+1]
                print("ALTERAÇÃO REALIZADA COM SUCESSO")
        else:
            print("Opção invalida")
    #Segundo as regras de validação, o sistema só pode finalizar digitando a opção 7 na tabela inicial ou digitando a senha errada 3 vezes. 
    #Portanto, esse elif envia o retorno que irá finalizar a função.
    elif (retornaN == "fimSenha"):
        return "encerrarSistema"

def excluiProduto():
    retornaN = validaSenha(listaCod,listaDescricao,listaQuant,contadorErrouSenha, contDigitacaoSenha)
    #O if a seguir serve para impedir a cuntinuidade do codigo caso um dos retornos sejam informados pela funcao
    if ((retornaN !="codNaoCadastrado") and (retornaN !="fimSenha")):
        excluirProduto = input("DESEJA EXCLUIR O PRODUTO? [S/N]: ")
        if (excluirProduto =="S" or excluirProduto == "s"):
            del listaCod[retornaN]
            del listaDescricao[retornaN]
            del listaQuant[retornaN]
            print("PRODUTO DELETADO COM SUCESSO!!\n")
        elif (excluirProduto =="N" or excluirProduto == "n"):
            print("OK, SEU PRODUTO NÃO FOI DELETADO")
        else:
            print("DESCULPE, NÃO ENTENDI SUA RESPOSTA. DIGITE S ou N")
    #Segundo as regras de validação, o sistema só pode finalizar digitando a opção 7 na tabela inicial ou digitando a senha errada 3 vezes. 
    #Portanto, esse elif envia o retorno que irá finalizar a função.
    elif (retornaN == "fimSenha"):
        return "encerrarSistema"

def listaEstoque():
    quantAbaixo100 = 0
    print(f'{"Código":^30}          {"Descrição":^30}        {"Quantidade":^49}')
    print("-"*130)

    for n in range(len(listaCod)):
        print(f"{listaCod[n]:^30}     |      {listaDescricao[n]:^30}       |        {listaQuant[n]:^30}")
        print("-"*130)
    print("Total de produtos cadastrados: ", len(listaCod))
    print("Quantidade de itens em estoque: ", sum(listaQuant))

    # Calculo de produtos que possuem menos de 100 unidades em estoque
    for n in listaQuant:
        if (n < 100):
            quantAbaixo100 += 1
    print("Produtos em estoque abaixo do mínimo permitido(100 unidades): ", quantAbaixo100)

def compraProduto():
    retornaN = validaCod(listaCod,listaDescricao,listaQuant)
    #O if a seguir serve para impedir a cuntinuidade do sistema, como nesse caso a senha não é requisitada, não utilizei fimSenha
    if retornaN !="codNaoCadastrado":
        comprar = int(input("Digite a quantidade de produtos que deseja comprar no estoque: "))
        if comprar <= 0:
            print("PRODUTO NÃO PODE SER COMPRADO POIS É MENOR OU IGUAL A ZERO")
        else:
            listaQuant[retornaN] += comprar
            print("PRODUTO COMPRADO COM SUCESSO")

def vendeProduto():
    retornaN = validaCod(listaCod,listaDescricao,listaQuant)
    #O if a seguir serve para impedir a cuntinuidade do sistema, como nesse caso a senha não é requisitada, não utilizei fimSenha
    if retornaN !="codNaoCadastrado":
        comprar = int(input("Digite a quantidade de produtos que deseja vender no estoque: "))

        if comprar <= 0:
            print("PRODUTO NÃO PODE SER COMPRADO POIS É MENOR OU IGUAL A ZERO")

        elif comprar <= listaQuant[retornaN]:
            listaQuant[retornaN] -= comprar
            print("PRODUTO VENDIDO COM SUCESSO")
        else:
            print("NÃO EXISTE ESSA QUANTIDADE NO ESTOQUE")

def inicio():
    print("----------XPTO----------\n1 - Cadastrar produto\n2 - Alterar produto\n3 - Excluir produto\n4 - Listar estoque de peças\n5 - Comprar produto\n6 - Vender produto\n7 - Sair  ")
    return (int(input("Digite umas das opções a cima\n")))

def sair():
    print("Saindo...")

while True:
    #Menu
    opcao = inicio()

    # Opções
    if (opcao==1):
        cadastraProduto()

    elif (opcao==2):
        encerrarSistema = alteraProduto()
        if encerrarSistema =="encerrarSistema":
            break
        contDigitacaoSenha += 1 # O contDigitacaoSenha acrescenta 1, fazendo com que o primeiro if da funcao validaSenha seja acionado (não pedindo a senha novamente)
    elif (opcao ==3):
        encerrarSistema = excluiProduto()
        #Segundo as regras de validação, o sistema só pode finalizar digitando a opção 7 na tabela inicial ou digitando a senha errada 3 vezes. 
        #Portanto, esse if finaliza o sistema
        if encerrarSistema =="encerrarSistema": #
            break
        contDigitacaoSenha += 1 # O cont2 acrescenta 1, fazendo com que o primeiro if da funcao validaSenha seja acionado (não pedindo a senha novamente)
    elif (opcao ==4):
        listaEstoque()

    elif (opcao ==5):
        compraProduto()

    elif (opcao ==6):
        vendeProduto()
            
    elif(opcao ==7):
        sair()
        break
    
    else:
        print("NUMERO NÃO RECONHECIDO...TENTE NOVAMENTE")
