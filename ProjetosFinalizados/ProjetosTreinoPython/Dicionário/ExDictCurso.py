
Pessoa1 = {}

while True:
    nome = input("Digite seu nome \n")
    Pessoa1['nome'] = nome

    AnoNasc = int(input("Digite seu ano de nascimento \n"))
    Pessoa1['Idade'] = 2020 - AnoNasc

    CTPS = int(input("Digite sua carteira de trabalho \n"))
    Pessoa1['CTPS'] = CTPS
    if CTPS == 0:
        print("Registro realizado, aqui as informações:")
        for k, v in Pessoa1.items():
            print(f"{k} é {v}")
        break
    else:
        AnoContra = int(input("Digite o seu ano de contratação \n"))
        Pessoa1['Ano de contratação'] = AnoContra

        Sal = int(input("Digite seu salário \n"))
        Pessoa1['Salário'] = Sal

        Pessoa1['Aposentadoria'] = ((AnoContra-AnoNasc) + 35)
        break

if CTPS != 0:
    for k,v in Pessoa1.items():
        print(f"{k} vale {v}")
    print("Funcionário cadastrado com SUCESSO.")