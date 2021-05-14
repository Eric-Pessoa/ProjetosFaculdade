lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

print(max(lista))

print(min(lista))

for n in lista:
    if n%2 == 0:
        print(n, end=" ")

print("\n")

count  = 0
for n in lista:
    if n == lista[0]:
        count += 1
print(f"O número de incidências do primeiro elemento da lista ({lista[0]}) foi {count}")

total = 0

for n in lista:
    total += n
print(total)

total2 = 0
for n in lista:
    if n < 0:
        total2 += n

print(total2)

print("fim :D")
