from grupo3 import *
from grupo4 import *
from grupo5 import *


codigoInscricao = []
nomesAluno = []
cpfAlunos = []
estadoAlunos = []
cursoAlunos = []
matAlunos = []


def inscricao():
    nomesAluno.append(str(input("Nome do aluno: ")))
    cpf = input("CPF(sem pontos ou traços): ").upper()
    validacao_cpf = validar_cpf(cpf)
    while validacao_cpf == False:
        print("CPF inválido. Digite novamente.")
        cpf = input("CPF(sem pontos ou traços): ").upper()
        validacao_cpf = validar_cpf(cpf)
    cpfAlunos.append(cpf)
    estado = input("Estado que deseja fazer o curso(Utilize as siglas em UF): ".upper())
    validacao_estado = validar_estado(estado)
    while validacao_estado == False:
        print("O Estado digitado não existe. Tente novamente.")
        estado = input("Estado que deseja fazer o curso: ").upper()
        validacao_estado = validar_estado(estado)
    estadoAlunos.append(estado)
    validacao_cod = mostrarCursos(estado)
    cod_curso = input("Escolha um dos cursos disponíveis pelo código: ").upper()
    while cod_curso not in validacao_cod:
        print("Por favor, digite um código válido. Tente novamente.")
        cod_curso = input("Escolha um dos cursos disponíveis pelo código: ").upper()
    cursoAlunos.append(cod_curso)
    codigoInscricao = list(enumerate(cpfAlunos, 1))
    numero_matricula = "rm"+str(codigoInscricao[-1][0])
    matAlunos.append(numero_matricula)
    print("Inscrição Aprovada", "número da matrícula: ", numero_matricula)
    return matAlunos, cpfAlunos


def alterar_inscricao_cpf(cpfAlunos):
    cpf = input("CPF(sem pontos ou traços): ")
    validacao_cpf = validar_cpf(cpf)
    while validacao_cpf == False:
        print("CPF inválido. Digite novamente.")
        cpf = input("CPF: ")
        validacao_cpf = validar_cpf(cpf)
    while cpf not in cpfAlunos:
        print("Esse CPF não está na nossa base de dados. Tente novamente.")
        cpf = input("CPF: ")
        validacao_cpf = validar_cpf(cpf)

    print("Matrícula: ", matAlunos[cpfAlunos.index(cpf)],"\nNome: ", nomesAluno[cpfAlunos.index(cpf)], "\nCurso: ", cursoAlunos[cpfAlunos.index(cpf)],"\n")
    estado = input("Digite o estado para a alteração do curso(Utilize as siglas em UF): ")

    validacao_estado = validar_estado(estado)
    while validacao_estado == False:
        print("O Estado digitado não existe. Tente novamente.")
        estado = input("Estado que deseja fazer o curso: ")
        validacao_estado = validar_estado(estado)
    estadoAlunos[cpfAlunos.index(cpf)] = estado

    validacao_cod = mostrarCursos(estado)
    cod_curso = input("Escolha um dos cursos disponíveis pelo código: ").upper()
    while cod_curso not in validacao_cod:
        print("Por favor, digite um código válido. Tente novamente.")
        cod_curso = input("Escolha um dos cursos disponíveis pelo código: ").upper()
    cursoAlunos[cpfAlunos.index(cpf)] = cod_curso

    print("Os dados foram alterados com sucesso!\nMatrícula: ", matAlunos[cpfAlunos.index(cpf)],"\nNome: ", nomesAluno[cpfAlunos.index(cpf)], "\nCurso: ", cursoAlunos[cpfAlunos.index(cpf)],"\n")

def alterar_inscricao_mat(matAlunos):
    mat = input("Digite a matrícula: ")
    while mat not in matAlunos:
        print("Essa matrícula não está na nossa base de dados. Tente novamente.")
        mat = input("Digite a matrícula: ")

    print("Matrícula: ", matAlunos[matAlunos.index(mat)],"\nNome: ", nomesAluno[matAlunos.index(mat)], "\nCurso: ", cursoAlunos[matAlunos.index(mat)],"\n")

    estado = input("Digite o estado para a alteração do curso(Utilize as siglas em UF): ")
    validacao_estado = validar_estado(estado)
    while validacao_estado == False:
        print("O Estado digitado não existe. Tente novamente.")
        estado = input("Estado que deseja fazer o curso: ")
        validacao_estado = validar_estado(estado)
    estadoAlunos[matAlunos.index(mat)] = estado

    validacao_cod = mostrarCursos(estado)
    cod_curso = input("Escolha um dos cursos disponíveis pelo código: ").upper()
    while cod_curso not in validacao_cod:
        print("Por favor, digite um código válido. Tente novamente.")
        cod_curso = input("Escolha um dos cursos disponíveis pelo código: ").upper()
    cursoAlunos[matAlunos.index(mat)] = cod_curso

    print("Os dados foram alterados com sucesso!\nMatrícula: ", matAlunos[matAlunos.index(mat)],"\nNome: ", nomesAluno[matAlunos.index(mat)], "\nCurso: ", cursoAlunos[matAlunos.index(mat)],"\n")





def listar_inscricoes():
    print("--------------------------------------------------------------","A01 – AI e Machine Learning","--------------------------------------------------------------",sep='\n')
    cadastrado = 0
    for index, item in enumerate(cursoAlunos):
        if item == "A01":
            cadastrado += 1
            print(index, " – ", nomesAluno[index])
    print("--------------------------------------------------------------")
    print("Total de inscritos: ", cadastrado)
    print("--------------------------------------------------------------","A02 – Business Intelligence","--------------------------------------------------------------",sep='\n')
    cadastrado = 0
    for index, item in enumerate(cursoAlunos):
        if item == "A02":
            cadastrado += 1
            print(index, " – ", nomesAluno[index])
    print("--------------------------------------------------------------")
    print("Total de inscritos: ", cadastrado)
    print("--------------------------------------------------------------","A03 – Governança em TI","--------------------------------------------------------------",sep='\n')
    cadastrado = 0
    for index, item in enumerate(cursoAlunos):
        if item == "A03":
            cadastrado += 1
            print(index, " – ", nomesAluno[index])
    print("--------------------------------------------------------------")
    print("Total de inscritos: ", cadastrado)
    print("--------------------------------------------------------------","A04 – Programação Python","--------------------------------------------------------------",sep='\n')
    cadastrado = 0
    for index, item in enumerate(cursoAlunos):
        if item == "A04":
            cadastrado += 1
            print(index, " – ", nomesAluno[index])
    print("--------------------------------------------------------------")
    print("Total de inscritos: ", cadastrado)
    print("--------------------------------------------------------------","A05 – Programação JAVA","--------------------------------------------------------------",sep='\n')
    cadastrado = 0
    for index, item in enumerate(cursoAlunos):
        if item == "A05":
            cadastrado += 1
            print(index, " – ", nomesAluno[index])
    print("--------------------------------------------------------------")
    print("Total de inscritos: ", cadastrado)

