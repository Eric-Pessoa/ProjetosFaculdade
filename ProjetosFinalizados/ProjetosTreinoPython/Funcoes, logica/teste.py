lista = []

def resposta(sim_nao):
    if(sim_nao == "sim"):
        lista.append(1)


print("telefonou para a vítima?")
sim_nao1 = input("")
resposta(sim_nao1)
print("Esteve no local do crime?")
sim_nao2 = input("")
resposta(sim_nao2)
print("Mora perto da vítimaw?")
sim_nao3 = input("")
resposta(sim_nao3)
print("Trabalhava com a vítima?")
sim_nao4 = input("")
resposta(sim_nao4)
print("Devia para a vítima?")
sim_nao5 = input("")
resposta(sim_nao5)


if (len(lista) < 2):
    print ("inocente")
elif (len(lista) == 2):
    print ("suspeito")
elif (len(lista) == 3 or len(lista) == 4):
    print ("cúmplice")
elif (len(lista) == 5):
    print ("culpado")


