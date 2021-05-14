from funcoes import ChecaSenha
from funcoes import Estoque0oumenos

print("Seja bem vindo ao controle de produtos da empresa XPTO. Escolha uma opção:")

listaCod = []
listaDescri = []
listaEstoq = []
cont = 0
cont2 = 0
cont3 = 0
contsenha = 0
senha = ""
MenorOuNao = ""


while True:
    print(" 1 - Cadastrar produto \n 2 - Alterar produto \n 3 - Excluir produto \n 4 - Listar estoque de peças \n 5 - Comprar produto \n 6 - Vender produto \n 7 - Sair")
    Escolha = input("")
    if(Escolha == "1"):
        print("Qual a quantidade de produtos no estoque que você quer cadastrar?")
        Estoque = int(input(""))
        okounao = Estoque0oumenos(Estoque)
        if(okounao != "ok"):
            print("Qual o código do produto que você quer cadastrar?")
            codigo = input("")
            if(codigo in listaCod):
                print("Não pode, esse código já está cadastrado na lista.")
            else:
                print("Qual a descrição do produto?")
                Descri = input("")
                listaCod.append(codigo)
                listaDescri.append(Descri)
                listaEstoq.append(Estoque)
                print("Produto cadastrado com sucesso.")
    if(Escolha == "2"):
        validacao = ChecaSenha(senha, contsenha, cont3)
        if (validacao == "fim"):
            break
        elif(validacao == "continua"):
            cont3 += 1
            print("Qual é o código do produto que quer alterar?")
            CodProd = input("")
            if (CodProd in listaCod):
                for n in range(0, len(listaCod)):
                    if (CodProd == listaCod[n]):
                        print("Descrição do código:",listaDescri[n])
                        print("Estoque do código:",listaEstoq[n])
                        print("O que você quer alterar? Se for a descrição digite 1, se for estoque digite 2.")
                        altera = input("")
                        if (altera == "1"):
                            print("Digite a nova descrição:")
                            Descri = input("")
                            listaDescri[n] = Descri
                            print("Alterado com sucesso.")
                        elif (altera == "2"):
                            print("Digite a nova quantidade no estoque:")
                            Estoque = int(input(""))
                            okounao = Estoque0oumenos(Estoque)
                            if (okounao != "ok"):
                                listaEstoq[n] = Estoque
                                print("Alterado com sucesso.")
            elif (CodProd not in listaCod):
                print("Produto não cadastrado.")
    if (Escolha == "3"):
        validacao = ChecaSenha(senha, contsenha,cont3)
        if (validacao == "fim"):
            break
        elif(validacao == "continua"):
            cont3 += 1
            print("Qual o código do produto a ser deletado?")
            CodProd = input("")
            if (CodProd in listaCod):
                for n in range(0, len(listaCod)):
                    if (CodProd == listaCod[n]):
                        print("Descrição do código:",listaDescri[n])
                        print("Estoque do produto:",listaEstoq[n])
                        print("Deseja deletar esse produto? 1 pra sim, 2 pra não")
                        opcao = input("")
                        if (opcao == "1"):
                            del listaCod[n]
                            del listaDescri[n]
                            del listaEstoq[n]
                            print("Produto excluído com sucesso.")
                            break
                        elif (opcao == "2"):
                            print("Ok, voltando ao menu.")
            elif(CodProd not in listaCod):
                print("Produto não cadastrado.")
    if (Escolha == "4"):
        print("CÓDIGO              DESCRIÇÃO                                  QUANTIDADE EM ESTOQUE: ")
        print("—————               —————————————                              ————————————————————————————— ")
        cont4 = 0
        cont100 = 0
        for n in range(0, len(listaCod)):
            print(listaCod[n], "               ", listaDescri[n], "                                            ",listaEstoq[n])
            cont4 = listaEstoq[n] + cont4
            if (listaEstoq[n] < 100):
                cont100 += 1

        print("Total de produtos cadastrados:", len(listaCod))
        print("Quantidade de itens em estoque:", cont4)
        print("Produtos com estoque abaixo do mínimo permitido (100 unidades);", cont100)
    if (Escolha == "5"):
        print("Qual o código do produto a ser comprado?")
        CodProd = input("")
        if (CodProd in listaCod):
            for n in range(0, len(listaCod)):
                if (CodProd == listaCod[n]):
                    print("Descrição do código:", listaDescri[n])
                    print("Estoque do produto:", listaEstoq[n])
                    print("Quantos produtos você quer comprar?")
                    Estoque = int(input(""))
                    okounao = Estoque0oumenos(Estoque)
                    if (okounao != "ok"):
                        ops = listaEstoq[n] + Estoque
                        listaEstoq[n] = ops
                        print("O novo total do produto é: ", ops)
        else:
            print("Produto não cadastrado")
    if (Escolha == "6"):
        print("Qual o código do produto que você quer alterar?")
        CodProd = input("")
        if (CodProd in listaCod):
            for n in range(0, len(listaCod)):
                if (CodProd == listaCod[n]):
                    print("Descrição do código:", listaDescri[n])
                    print("Estoque do produto:", listaEstoq[n])
                    print("Quantos produtos você quer vender??")
                    Estoque = int(input(""))
                    if(listaEstoq[n] < Estoque):
                        print("Não dá pra vender mais do que se tem em estoque.")
                    else:
                        okounao = Estoque0oumenos(Estoque)
                        if (okounao != "ok"):
                            ops2 = listaEstoq[n] - Estoque
                            listaEstoq[n] = ops2
                            print("O novo total do produto é: ", ops2)
        else:
            print("Produto não cadastrado.")
    if (Escolha == "7"):
        print("Programa finalizado.")
        break