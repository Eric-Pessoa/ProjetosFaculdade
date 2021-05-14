preco = (10.75,9.78,100.60)
def prog (lista):
    count = 0
    SOMA = 0
    print("  ----------------------------------\n ", "  Lista de preços\n ", "----------------------------------")
    for i in lista:
        count += 1
        print(" PRODUTO", count,"................", i)
        SOMA += i
    print("----------------------------------\n", "TOTAL", "................",SOMA)
prog(preco)

#Isso aqui foi um teste pra treinar com listas