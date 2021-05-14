
''''
DadosEscolares = {'Eric':'fiap','pedro':'abc','joao':'123','bruna':'234','abacate':'333'}

#tentando pegar um nome da lista
print("Digite um nome")
n = input("")

if n in DadosEscolares:
    print(DadosEscolares.get(n))


Ano = {2002:'Robert'}
Ano2 = {2003:'julia'}
Ano3 = {2004:'ademin'}


dados = dict(A = Ano,B = Ano2, C = Ano3)

print(dados.keys())


dados = {'A':{2002:'robert'}}

print(dados.get('A'))

'''



