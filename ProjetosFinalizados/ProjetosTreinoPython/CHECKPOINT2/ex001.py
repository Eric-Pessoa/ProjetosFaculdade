


SalaFixo = float(1585.00)

#Listas vendedores
VendedoresNome = []
VendedoresCod = []

#Lista de vendas de cada vendedor

ListaTemp = []
VendasVend1 = []
VendasVend2 = []
VendasVend3 = []
VendasVend4 = []
VendasVend5 = []

#Listas produtos
ListaProdutos = []
CodProdutos = []
ValorUnitarioProdutos = []
DescProdutos = []


def inicio():
    print(" Bom dia, selecione uma opção: \n")
    print(" 1 - Cadastrar vendedores \n")
    print(" 2 - Cadastrar produtos \n")
    print(" 3 - Vender produtos \n")
    print(" 4 - Listar produtos vendidos por vendedor \n")
    print(" 5 - sair \n")

    return int(input("Digite a opção que você quer: "))


def CadastrarVendedores():
    if(len(VendedoresCod) == 5):
        print("Já foi cadastrado o número máximo de vendedores possíveis.")
    else:
        for n in range(5):
            VendNome = input("Digite o nome do vendedor: \n")
            VendCod =  int(input("Digite o código do vendedor: \n"))
            if(VendCod < 0):
                print("O código do vendedor não pode ser menor que 0")
            elif(VendCod in VendedoresCod):
                print("O código desse vendedor é idêntico a de outro vendedor existente. Isso é proibido. Vendedor não cadastrado.")
            elif(VendCod not in VendedoresCod):
                VendedoresNome.append(VendNome)
                VendedoresCod.append(VendCod)

def CadastrarProdutos():
        if (len(CodProdutos) == 3):
            print("Produtos já cadastrados, não se pode cadastrar novamente.")
        else:
            for n in range(3):
                ProdCod = int(input("Digite o código do produto: \n"))
                ProdDesc = input("Digite a descrição do produto: \n")
                ProdValorUnitario = int(input("Digite o valor unitário do produto: \n"))
                if (ProdCod < 0):
                    print("O código do produto não pode ser menor que 0")
                elif (ProdCod in CodProdutos):
                    print("O código desse produto é idêntico a de outro produto existente. Isso é proibido. Produto não cadastrado.")
                elif (ProdCod not in CodProdutos):
                    CodProdutos.append(ProdCod)
                    ListaTemp.append(ProdCod) #00
                    ListaTemp.append(ProdDesc) #01
                    ListaTemp.append(ProdValorUnitario) #02
                    ListaProdutos.append(ListaTemp[:])
                    ListaTemp.clear()


def VenderProdutos():
    while True:
        if(VendedoresCod == [] or ListaProdutos == []):
            print("Não se pode acessar essa opção sem ter cadastrado no mínimo 1 funcionário e 1 produto.")
            break
        ProdCod = int(input("Digite o código do produto que deseja vender: \n"))
        if(ProdCod not in CodProdutos):
            print("O código desse produto não foi cadastrado, retornando ao menu.")
            break
        QntdVendaProd = int(input("Digite a quantidade de produtos que deseja vender: \n"))
        if(QntdVendaProd <= 0):
            print("Não se dá pra vender 0 ou menos produtos, retornando ao menu.")
            break
        VendCod = int(input("Digite o código do vendedor do produto: \n"))
        if(VendCod not in VendedoresCod):
            print("Não existe nenhum vendedor com esse código cadastrado no sistema.")
            break

        if (VendCod == VendedoresCod[0]):
            count = 0
            ListaTemp.append(ProdCod) #00
            count2 = 0
            for n in ListaProdutos:
                if (ListaProdutos[count2][0] == ProdCod):
                    ListaTemp.append(ListaProdutos[count2][1]) #01
                    ListaTemp.append(ListaProdutos[count2][2]) #02
                    count2 += 1
                else:
                    count2 += 1
            ListaTemp.append(QntdVendaProd) #03
            ListaTemp.append(VendCod) #04
            for n in VendasVend1:
                if (VendasVend1[count][0] == ProdCod):
                    VendasVend1[count][3] += QntdVendaProd
                    ListaTemp.clear()
                    break
                else:
                    count += 1
            if(ListaTemp == []):
                break
            else:
                VendasVend1.append(ListaTemp[:])
                ListaTemp.clear()
                break


        elif(VendCod == VendedoresCod[1]):
            count = 0
            ListaTemp.append(ProdCod) #00
            count2 = 0
            for n in ListaProdutos:
                if (ListaProdutos[count2][0] == ProdCod):
                    ListaTemp.append(ListaProdutos[count2][1]) #01
                    ListaTemp.append(ListaProdutos[count2][2]) #02
                    count2 += 1
                else:
                    count2 += 1
            ListaTemp.append(QntdVendaProd) #03
            ListaTemp.append(VendCod) #04
            for n in VendasVend2:
                if (VendasVend2[count][0] == ProdCod):
                    VendasVend2[count][3] += QntdVendaProd
                    ListaTemp.clear()
                    break
                else:
                    count += 1
            if(ListaTemp == []):
                break
            else:
                VendasVend2.append(ListaTemp[:])
                ListaTemp.clear()
                break
        elif(VendCod == VendedoresCod[2]):
            count = 0
            ListaTemp.append(ProdCod) #00
            count2 = 0
            for n in ListaProdutos:
                if (ListaProdutos[count2][0] == ProdCod):
                    ListaTemp.append(ListaProdutos[count2][1]) #01
                    ListaTemp.append(ListaProdutos[count2][2]) #02
                    count2 += 1
                else:
                    count2 += 1
            ListaTemp.append(QntdVendaProd) #03
            ListaTemp.append(VendCod) #04
            for n in VendasVend3:
                if (VendasVend3[count][0] == ProdCod):
                    VendasVend3[count][3] += QntdVendaProd
                    ListaTemp.clear()
                    break
                else:
                    count += 1
            if(ListaTemp == []):
                break
            else:
                VendasVend3.append(ListaTemp[:])
                ListaTemp.clear()
                break

        elif (VendCod == VendedoresCod[3]):
            count = 0
            ListaTemp.append(ProdCod) #00
            count2 = 0
            for n in ListaProdutos:
                if (ListaProdutos[count2][0] == ProdCod):
                    ListaTemp.append(ListaProdutos[count2][1]) #01
                    ListaTemp.append(ListaProdutos[count2][2]) #02
                    count2 += 1
                else:
                    count2 += 1
            ListaTemp.append(QntdVendaProd) #03
            ListaTemp.append(VendCod) #04
            for n in VendasVend4:
                if (VendasVend4[count][0] == ProdCod):
                    VendasVend4[count][3] += QntdVendaProd
                    ListaTemp.clear()
                    break
                else:
                    count += 1
            if(ListaTemp == []):
                break
            else:
                VendasVend4.append(ListaTemp[:])
                ListaTemp.clear()
                break

        elif (VendCod == VendedoresCod[4]):
            count = 0
            ListaTemp.append(ProdCod) #00
            count2 = 0
            for n in ListaProdutos:
                if (ListaProdutos[count2][0] == ProdCod):
                    ListaTemp.append(ListaProdutos[count2][1]) #01
                    ListaTemp.append(ListaProdutos[count2][2]) #02
                    count2 += 1
                else:
                    count2 += 1
            ListaTemp.append(QntdVendaProd) #03
            ListaTemp.append(VendCod) #04
            for n in VendasVend5:
                if (VendasVend5[count][0] == ProdCod):
                    VendasVend5[count][3] += QntdVendaProd
                    ListaTemp.clear()
                    break
                else:
                    count += 1
            if(ListaTemp == []):
                break
            else:
                VendasVend5.append(ListaTemp[:])
                ListaTemp.clear()
                break


def ProdutosVendidosPorVendedor():

    for n in range (5):
        print(f"Vendedor: {VendedoresCod[n]} - {VendedoresNome[n]}")
        if(n == 0):
            if(VendasVend1 != []):
                countVend = 0
                ValorTotalItem = 0
                SomaGeral = 0
                print(f"\n Código do produto-----Descrição do produto------Valor Unitário------Quantidade vendida------Valor total")
                for y in VendasVend1:
                    ValorTotalItem += VendasVend1[countVend][2] * VendasVend1[countVend][3]
                    print(f"        {VendasVend1[countVend][0]}                       {VendasVend1[countVend][1]}                       {VendasVend1[countVend][2]}                    {VendasVend1[countVend][3]}                  {ValorTotalItem}\n")
                    countVend += 1
                    SomaGeral += ValorTotalItem
                    ValorTotalItem = 0
                print(f"Valor total das vendas - {VendedoresNome[n]}: {SomaGeral}")
                comissao1 = SomaGeral * 0.05
                print(f"A comissão recebida foi: {comissao1}")
                print(f"Salário do mês (fixo + comissão): {SalaFixo + comissao1} \n")
            else:
                print("Nenhuma")
        if(n == 1):
            if(VendasVend2 != []):
                countVend = 0
                ValorTotalItem = 0
                SomaGeral = 0
                print(f"\n Código do produto-----Descrição do produto------Valor Unitário------Quantidade vendida------Valor total")
                for y in VendasVend2:
                    ValorTotalItem += VendasVend2[countVend][2] * VendasVend2[countVend][3]
                    print(f"        {VendasVend2[countVend][0]}                       {VendasVend2[countVend][1]}                       {VendasVend2[countVend][2]}                    {VendasVend2[countVend][3]}                  {ValorTotalItem}\n")
                    countVend += 1
                    SomaGeral += ValorTotalItem
                    ValorTotalItem = 0
                print(f"Valor total das vendas - {VendedoresNome[n]}: {SomaGeral}")
                comissao2 = SomaGeral * 0.05
                print(f"A comissão recebida foi: {comissao2}")
                print(f"Salário do mês (fixo + comissão): {SalaFixo + comissao2} \n")
            else:
                print("Nenhuma")


        if(n == 2):
            if(VendasVend3 != []):
                countVend = 0
                ValorTotalItem = 0
                SomaGeral = 0
                print(f"\n Código do produto-----Descrição do produto------Valor Unitário------Quantidade vendida------Valor total")
                for y in VendasVend3:
                    ValorTotalItem += VendasVend3[countVend][2] * VendasVend3[countVend][3]
                    print(f"        {VendasVend3[countVend][0]}                       {VendasVend3[countVend][1]}                       {VendasVend3[countVend][2]}                    {VendasVend3[countVend][3]}                  {ValorTotalItem}\n")
                    countVend += 1
                    SomaGeral += ValorTotalItem
                    ValorTotalItem = 0
                print(f"Valor total das vendas - {VendedoresNome[n]}: {SomaGeral}")
                comissao3 = SomaGeral * 0.05
                print(f"A comissão recebida foi: {comissao3}")
                print(f"Salário do mês (fixo + comissão): {SalaFixo + comissao3} \n")
            else:
                print("Nenhuma")

        if(n == 3):
            if(VendasVend4 != []):
                countVend = 0
                ValorTotalItem = 0
                SomaGeral = 0
                print(f"\n Código do produto-----Descrição do produto------Valor Unitário------Quantidade vendida------Valor total")
                for y in VendasVend4:
                    ValorTotalItem += VendasVend4[countVend][2] * VendasVend4[countVend][3]
                    print(f"        {VendasVend4[countVend][0]}                       {VendasVend4[countVend][1]}                       {VendasVend4[countVend][2]}                    {VendasVend4[countVend][3]}                  {ValorTotalItem}\n")
                    countVend += 1
                    SomaGeral += ValorTotalItem
                    ValorTotalItem = 0
                print(f"Valor total das vendas - {VendedoresNome[n]}: {SomaGeral}")
                comissao4 = SomaGeral * 0.05
                print(f"A comissão recebida foi: {comissao4}")
                print(f"Salário do mês (fixo + comissão): {SalaFixo + comissao4} \n")
            else:
                print("Nenhuma")

        if(n == 4):
            if(VendasVend5 != []):
                countVend = 0
                ValorTotalItem = 0
                SomaGeral = 0
                print(f"\n Código do produto-----Descrição do produto------Valor Unitário------Quantidade vendida------Valor total")
                for y in VendasVend5:
                    ValorTotalItem += VendasVend5[countVend][2] * VendasVend5[countVend][3]
                    print(f"        {VendasVend5[countVend][0]}                       {VendasVend5[countVend][1]}                       {VendasVend5[countVend][2]}                    {VendasVend5[countVend][3]}                  {ValorTotalItem}\n")
                    countVend += 1
                    SomaGeral += ValorTotalItem
                    ValorTotalItem = 0
                print(f"Valor total das vendas - {VendedoresNome[n]}: {SomaGeral}")
                comissao5 = SomaGeral * 0.05
                print(f"A comissão recebida foi: {comissao5}")
                print(f"Salário do mês (fixo + comissão): {SalaFixo + comissao5} \n")
            else:
                print("Nenhuma")




def sair():
    print("Saindo...")



while True:

    opcao = inicio()

    if(opcao == 1):
        CadastrarVendedores()

    if(opcao == 2):
        CadastrarProdutos()

    if(opcao == 3):
        VenderProdutos()

    if(opcao == 4):
        ProdutosVendidosPorVendedor()

    if(opcao == 5):
        sair()
        break


