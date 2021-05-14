lista1 = []
lista2 = []
Peso = []
pessoasPeso = []
pessoasLeve = []


for n in range(0,2):
    lista1.append(input("Digite seu nome: \n"))
    lista1.append(int(input("Digite seu peso: \n")))
    lista2.append(lista1[:])
    lista1.clear()


for n in lista2:
    Peso.append(n[1])

    
'''''''''
for n in lista2:
    for y in n:
        Pessoas.append(y)

for n,v in enumerate(Pessoas):
    if n%2 == 0:
        Pessoas.pop(n)
'''''

print(f"Número de pessoas cadastradas foi: {len(lista2)}")
print(lista2)