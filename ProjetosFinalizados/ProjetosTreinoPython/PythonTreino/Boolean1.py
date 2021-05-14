print("Informe o valor do seu salário e da prestação do seu empréstimo")

sal = float(input(""))
prest = float(input(""))

limite = sal * 0.30

permitido = prest <= limite

if(permitido):
    print("pode pa cachorro") 
else:
    print("ai não meu mano")