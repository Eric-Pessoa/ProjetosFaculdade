print("Bem vindo ao portal. Aqui você consegue ver a situação acadêmica de um aluno, se ele foi aprovado, reprovado por falta, ou reprovado por média.")
print("Digite o nome do aluno desejado, suas 3 notas na matéria, e o número de faltas que ele tem.")
Nome = input("Nome do aluno: ")
Nota1 = int(input("Digite a primeira nota: "))
Nota2 = int(input("Digite a segunda nota: "))
Nota3 = int(input("Digite a terceira nota: "))
Falta = int(input("Digite o número de faltas do aluno: "))


if((Nota1 + Nota2 + Nota3 / 3) >= 7 and Falta <= 20):
    print("Você passou.")
elif(Falta > 20):
    print("Reprovado por falta.")
else:
    print("Reprovado por média.")
    