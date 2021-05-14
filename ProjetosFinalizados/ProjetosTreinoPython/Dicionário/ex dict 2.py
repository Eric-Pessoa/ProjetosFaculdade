
import random


#Geral['jogador1'] = random.randint(1, 6)
#Geral['jogador2'] = random.randint(1, 6)
#Geral['jogador3'] = random.randint(1, 6)
#Geral['jogador4'] = random.randint(1, 6)

var1 = random.randint(1,6)
var2 = random.randint(1,6)
var3 = random.randint(1,6)
var4 = random.randint(1,6)


lista = [{'jogador':var1},
        {'jogador':var2},
        {'jogador':var3},
        {'jogador':var4}]


sorted_list = sorted(lista, key=lambda k: k['jogador'], reverse=True)
num = 1

for n in sorted_list:
    for k,v in n.items():
        print(f"{k} {num} teve {v} pontos, e ficou em {num} lugar")
        num += 1



#print(sorted_list)

