
print("Olá, me informe 4 notas que irei te informar a média aritimética delas.")

notas = []
elemento = 1

for n in range (0,4):
    print(f"Qual a nota {elemento}?")
    resposta = int(input(""))
    notas.append(resposta)
    elemento += 1


soma = sum(notas)

count = 0
for n in notas:
    count += 1

result = soma/count

print(result)