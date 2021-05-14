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



    def Checar(identificacao):
        if identificacao in esferaID:
            return "NaoCadastrarEsfera"
        elif identificacao in limpezaID:
            return "NaoCadastrarLimpeza"
        elif identificacao in cabo_conectorID:
            return "NaoCadastrarCaboConector"
        elif identificacao in quebrado_inutilizID:
            return "NaoCadastrarQuebrado"
        elif identificacao in Mouse_sem_defeitoID:
            return "NaoCadastrarSemDefeito"


    continuar = True
    print("Para encerrar digite 0 na identificação!")
    while continuar == True:
        identificacao = int(input("Digite o número de identificação do mouse: "))
        if identificacao in quebrado_inutilizID  or identificacao in Mouse_sem_defeitoID:
            print("Não se pode cadastrar outro defeito para um mouse que já foi cadastrado como bom, ou um mouse que já deu perda total.")
        elif (identificacao == 0):  # FINALIZA
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
            testando = Checar(identificacao)
            while entrada < 0 or entrada > 5 or entrada == None:
                entrada = int(input("Resposta Inválida. Digite novamente! Situação: "))

            if entrada == 1 and testando == "NaoCadastrarEsfera":
                print("Impossível, você já cadastrou esse erro pra esse mouse.")
                id.pop()
            elif entrada == 2 and testando == "NaoCadastrarLimpeza":
                print("Impossível, você já cadastrou esse erro pra esse mouse.")
                id.pop()
            elif entrada == 3 and testando == "NaoCadastrarCaboConector":
                print("Impossível, você já cadastrou esse erro pra esse mouse.")
                id.pop()
            elif entrada == 4 and testando == "NaoCadastrarQuebrado":
                print("Impossível, você já cadastrou esse erro pra esse mouse.")
                id.pop()
            elif entrada == 5 and testando == "NaoCadastrarSemDefeito":
                print("Impossível, você já cadastrou esse erro pra esse mouse.")
                id.pop()
            else:
                esfera, limpeza, cabo_conector, quebrado_inutiliz, Mouse_sem_defeito = classificar(identificacao, entrada, esfera, limpeza, cabo_conector,
                                                                                quebrado_inutiliz, Mouse_sem_defeito)

    totalGeral = esfera + limpeza + cabo_conector + quebrado_inutiliz + Mouse_sem_defeito

    if (totalGeral != 0):

        print("\nResumo")
        print(f"Número total de mouses cadastrados:{len(id)}")
        if(Mouse_sem_defeitoID == []):
            print("Nenhum mouse sem defeito foi cadastrado.")
        else:
            print(f"% de mouses sem defeito: {len(id)/len(Mouse_sem_defeitoID)}")


        def countesfera (esferaID,limpezaID,cabo_conectorID,quebrado_inutilizID,Mouse_sem_defeitoID):
            VarEsfera = set(esferaID) - set(limpezaID) - set(cabo_conectorID) - set(quebrado_inutilizID) - set(Mouse_sem_defeitoID)
            return len(VarEsfera)
        def countlimpeza (esferaID,limpezaID,cabo_conectorID,quebrado_inutilizID,Mouse_sem_defeitoID):
            VarLimpeza = set(limpezaID) - set(esferaID) - set(cabo_conectorID) - set(quebrado_inutilizID) - set(Mouse_sem_defeitoID)
            return len(VarLimpeza)
        def countcaboconector (esferaID,limpezaID,cabo_conectorID,quebrado_inutilizID,Mouse_sem_defeitoID):
            VarCabo = set(cabo_conectorID) - set(limpezaID) - set(esferaID) - set(quebrado_inutilizID) - set(Mouse_sem_defeitoID)
            return len(VarCabo)
        def countquebrado (quebrado_inutilizID):
            VarQuebrado = set(quebrado_inutilizID)
            return len(VarQuebrado)
        def countsemdefeito (Mouse_sem_defeitoID):
            VarSemDefeito = set(Mouse_sem_defeitoID)
            return len(VarSemDefeito)



        contesferaunique = countesfera(esferaID,limpezaID,cabo_conectorID,quebrado_inutilizID,Mouse_sem_defeitoID)
        contlimpezaunique = countlimpeza(esferaID,limpezaID,cabo_conectorID,quebrado_inutilizID,Mouse_sem_defeitoID)
        contcaboconectorunique = countcaboconector(esferaID,limpezaID,cabo_conectorID,quebrado_inutilizID,Mouse_sem_defeitoID)
        contquebrado = countquebrado(quebrado_inutilizID)
        contsemdefeito = countsemdefeito(Mouse_sem_defeitoID)




        print(f"% de mouses com apenas um defeito: {(len(id) / (contesferaunique + contlimpezaunique + contcaboconectorunique + contquebrado + contsemdefeito))}")

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








    #    print("\nQuantidade de mouses: ", total, "\n\nSituação\t\t\t\t\t\t\t\t\t\t\tQuantidade\t\t\t\tPercentual")
    #    print("\n1 - Necessita da esfera\t\t\t\t\t\t\t\t", esfera, "\t\t\t\t\t\t", esfera * 100 / total, "%")
    #    print("2 - Necessita da limpeza\t\t\t\t\t\t\t", limpeza, "\t\t\t\t\t\t", limpeza * 100 / total, "%")
    #    print("3 - Necessita de troca do cabo ou conector\t\t\t", cabo_conector, "\t\t\t\t\t\t",
    #         cabo_conector * 100 / total, "%")
    #    print("4 - Quebrado ou inutilizado\t\t\t\t\t\t\t", quebrado_inutiliz, "\t\t\t\t\t\t",
    #          quebrado_inutiliz * 100 / total, "%")


ex4b()
