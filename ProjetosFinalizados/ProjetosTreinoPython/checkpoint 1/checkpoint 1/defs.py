#Essa funçao apresenta a validação de senha
def validaSenha(lista_Cod,lista_Descricao,lista_quant,contadorErrouSenha, contDigitacaoSenha):
    
    while True:
        #aqui é caso a senha já tenha sido informada corretamente uma vez.
        if (contDigitacaoSenha >=1):
            cod_Prod = int(input("Digite o codigo do produto para verificação: "))
            if cod_Prod not in lista_Cod:
                    print("PRODUTO NÃO CADASTRADO")
                    return "codNaoCadastrado"
            for n in range(len(lista_Cod)):
                if cod_Prod ==lista_Cod[n]:
                    print(f"A descrição do produto com código {cod_Prod} é:")
                    print("-"*30,"\n", {lista_Descricao[n]}) 
                    print("-"*30)
                    print(f"A quantidade de produtos cadastrados com o código {cod_Prod} é:")
                    print("-"*30, "\n", {lista_quant[n]})
                    print("-"*30,"\n")
                    #retornamos o valor n para ele poder ser armazenado em uma variável pra função alteraproduto.
                    return n
        #aqui é caso a senha correta ainda não tenha sido digitada pelo usuário.
        senha = input("Digite a senha de acesso: ")
        if (senha == "yN1825*a"):
            cod_Prod = int(input("Digite o codigo do produto para verificação: "))
            if cod_Prod not in lista_Cod:
                    print("PRODUTO NÃO CADASTRADO")
                    return "codNaoCadastrado"
            for n in range(len(lista_Cod)):
                if cod_Prod ==lista_Cod[n]:
                    print(f"A descrição do produto com código {cod_Prod} é:")
                    print("-"*30,"\n", {lista_Descricao[n]}) 
                    print("-"*30)
                    print(f"A quantidade de produtos cadastrados com o código {cod_Prod} é:")
                    print("-"*30, "\n", {lista_quant[n]})
                    print("-"*30,"\n")
                    #retornamos o valor n para ele poder ser armazenado em uma variável pra função alteraproduto.
                    return n
        else:
            if (contadorErrouSenha >=2):
                print("SEU ACESSO FOI BLOQUEADO! PROCURE O ADMINISTRADOR")
                return "fimSenha"
            else:
                print("SENHA INCORRETA")
                contadorErrouSenha +=1

#Essa funcao não apresenta a validação de senha
def validaCod(lista_Cod,lista_Descricao,lista_quant):
    cod_Prod = int(input("Digite o codigo do produto para verificação: "))
    if cod_Prod not in lista_Cod:
        print("PRODUTO NÃO CADASTRADO")
        return "codNaoCadastrado"
    for n in range(len(lista_Cod)):
        if cod_Prod ==lista_Cod[n]:
            print(f"A descrição do produto com código {cod_Prod} é:")
            print("-"*30,"\n", {lista_Descricao[n]}) 
            print("-"*30)
            print(f"A quantidade de produtos cadastrados com o código {cod_Prod} é:")
            print("-"*30, "\n", {lista_quant[n]})
            print("-"*30,"\n")
            return n