def ex4b():
    esfera = 0
    limpeza = 0
    cabo_conector = 0
    quebrado_inutiliz = 0
    Mouse_sem_defeito = 0
    esferaID = []
    limpezaID = []
    cabo_conectorID = []
    quebrado_inutilizID = []
    Mouse_sem_defeitoID = []
    id = []

    def classificar(identificacao, defeito, esfera, limpeza, cabo_conector, quebrado_inutiliz, Mouse_sem_defeito):
        if defeito == 1:
            esfera += 1
            esferaID.append(identificacao)
        elif defeito == 2:
            limpeza += 1
            limpezaID.append(identificacao)
        elif defeito == 3:
            cabo_conector += 1
            cabo_conectorID.append(identificacao)
        elif defeito == 4:
            quebrado_inutiliz += 1
            quebrado_inutilizID.append(identificacao)
        elif defeito == 5:
            Mouse_sem_defeito += 1
            Mouse_sem_defeitoID.append(identificacao)
        return esfera, limpeza, cabo_conector, quebrado_inutiliz, Mouse_sem_defeito

    continuar = True
    print("Para encerrar digite 0 na identificação!")
    while continuar == True:
        identificacao = int(input("Digite o número de identificação do mouse: "));
        if (identificacao == 0):  # FINALIZA
            continuar = False
        else:
            id.append(identificacao)
            print("", "-" * 30, "\n           Mouse", "\n", "-" * 30,
                  "\n1 -> necessita da esfera"
                  "\n2 -> necessita de limpeza"
                  "\n3 -> necessita troca do cabo ou conector"
                  "\n4 -> quebrado ou inutilizado"
                  "\n5 -> Não apresenta problemas")
            entrada = int(input("Situação: "))
            while entrada < 0 or entrada > 5 or entrada == None:
                entrada = int(input("Resposta Inválida. Digite novamente! Situação: "))

            esfera, limpeza, cabo_conector, quebrado_inutiliz, Mouse_sem_defeito = classificar(identificacao, entrada, esfera, limpeza, cabo_conector,
                                                                            quebrado_inutiliz, Mouse_sem_defeito)

    totalGeral = esfera + limpeza + cabo_conector + quebrado_inutiliz + Mouse_sem_defeito

    if (totalGeral != 0):
        print("\n ----","Identificação dos mouses sem defeito","---- \n")
        if(Mouse_sem_defeitoID  == []):
            print("Nenhum")
        else:
            for n in Mouse_sem_defeitoID:
                print(n, end=" ")
        print("\n")
        print("Total: ", Mouse_sem_defeito, "mouses")

        print("\n ----", "Identificação dos mouses que necessitam de esfera", "---- \n")
        if (esferaID == []):
            print("Nenhum")
        else:
            for n in esferaID:
                print(n, end=" ")
        print("\n")
        print("Total: ", esfera, "mouses")

        print("\n ----", "Identificação dos mouses que necessitam de limpeza", "---- \n")
        if (limpezaID == []):
            print("Nenhum")
        else:
            for n in limpezaID:
                print(n, end=" ")
        print("\n")
        print("Total: ", limpeza, "mouses")

        print("\n ----", "Identificação dos mouses que necessitam troca de cabo ou conector", "---- \n")
        if (cabo_conectorID == []):
            print("Nenhum")
        else:
            for n in cabo_conectorID:
                print(n, end=" ")
        print("\n")
        print("Total: ", cabo_conector, "mouses")

        print("\n ----", "Identificação dos mouses que estão quebrados ou inutilizados", "---- \n")
        if (Mouse_sem_defeitoID == []):
            print("Nenhum")
        else:
            for n in quebrado_inutilizID:
                print(n, end=" ")
        print("\n")
        print("Total: ", quebrado_inutiliz, "mouses")




#tá errado, mas eu quase acertei a lógica



    #    print("\nQuantidade de mouses: ", total, "\n\nSituação\t\t\t\t\t\t\t\t\t\t\tQuantidade\t\t\t\tPercentual")
    #    print("\n1 - Necessita da esfera\t\t\t\t\t\t\t\t", esfera, "\t\t\t\t\t\t", esfera * 100 / total, "%")
    #    print("2 - Necessita da limpeza\t\t\t\t\t\t\t", limpeza, "\t\t\t\t\t\t", limpeza * 100 / total, "%")
    #    print("3 - Necessita de troca do cabo ou conector\t\t\t", cabo_conector, "\t\t\t\t\t\t",
    #         cabo_conector * 100 / total, "%")
    #    print("4 - Quebrado ou inutilizado\t\t\t\t\t\t\t", quebrado_inutiliz, "\t\t\t\t\t\t",
    #          quebrado_inutiliz * 100 / total, "%")


ex4b()
