

dadosValue = {}

DadosNome = {}

print("Bem vindo, cadastre pessoas!")

nome = input("Digite seu nome: \n")
idade = int(input("Digite sua idade: \n"))
cidade = input("Digite sua cidade: \n")
dadosValue[idade] = cidade

DadosNome[nome] = dadosValue




for n in DadosNome.keys():
    print("Nome: ", n)

for n in dadosValue.keys():
    print("Idade: ",  n)

for n in dadosValue.values():
    print("Cidade: ", n)