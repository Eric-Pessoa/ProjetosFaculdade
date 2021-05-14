import re
from grupo4 import *


codigoInscricao = []
nomesAluno = []
cpfAlunos = []
estadoAlunos = []
capitais = ["AM", "Manaus", "RR", "Boa Vista", "PA", "Belém", "AP", "Macapá", "TO", "Palmas", "RO", "Porto Velho", "AC",
            "Rio Branco", "MA", "São Luís", "PI", "Teresina", "CE", "Fortaleza", "RN", "Natal", "PE", "Recife", "PB",
            "João Pessoa", "SE", "Aracaju", "AL", "Maceió", "BA", "Salvador", "MT", "Cuiabá", "MS", "Campo Grande",
            "GO", "Goiânia", "DF", "Brasília", "SP", "São Paulo", "RJ", "Rio de Janeiro", "ES", "Vitória", "MG",
            "Belo Horizonte", "PR", "Curitiba", "RS", "Porto Alegre", "SC", "Florianópolis"]
capitaisAlunos = []
cursoAlunos = []
matAlunos = []



def chamar_menu():
    menu = ("1. Fazer Inscrição","2. Alterar Inscrição","3. Listar Inscrições","4. Sair")
    print("-" * 25)
    print("{:^25}".format(" MENU "))
    print("-" * 25)
    for item in menu:
        print(f"{item:25}")
    opcao = input("Escolha: ")
    return opcao



def inscricao():
    nomesAluno.append(str(input("\nNome do aluno: ")))
    cpf = input("CPF(sem pontos ou traços): ")
    while cpf in cpfAlunos:
        print("Aluno já cadastrado em outro curso.")
        cpf = input("CPF(sem pontos ou traços): ")
    validacao_cpf = validar_cpf(cpf)
    while validacao_cpf == False:
        print("CPF inválido. Digite novamente.")
        cpf = input("CPF(sem pontos ou traços): ").upper()
        validacao_cpf = validar_cpf(cpf)
    cpfAlunos.append(cpf)
    estado = input("Estado que deseja fazer o curso(Utilize as siglas em UF): ").upper()
    validacao_estado = validar_estado(estado)
    while validacao_estado == False:
        print("O Estado digitado não existe. Tente novamente.")
        estado = input("Estado que deseja fazer o curso: ").upper()
        validacao_estado = validar_estado(estado)
    estadoAlunos.append(estado)
    for cap in capitais:
        if cap == estado:
            capital = capitais[capitais.index(cap)+1]
            capitaisAlunos.append(capital)
            break
    validacao_cod = mostrarCursos(estado)
    cod_curso = input("Escolha um dos cursos disponíveis pelo código: ").upper()
    while cod_curso not in validacao_cod:
        print("Por favor, digite um código válido. Tente novamente.")
        cod_curso = input("Escolha um dos cursos disponíveis pelo código: ").upper()
    cursoAlunos.append(cod_curso)
    codigoInscricao = list(enumerate(cpfAlunos, 1))
    numero_matricula = "rm"+str(codigoInscricao[-1][0])
    matAlunos.append(numero_matricula)
    print(f"Inscrição Aprovada. Número de matrícula: {numero_matricula}")
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
    if estado in capitais and len(capitaisAlunos)!=0: #inclusao
         capitaisAlunos[cpfAlunos.index(cpf)]=capitais[capitais.index(estado)+1] #inclusao

    print("Os dados foram alterados com sucesso!\nMatrícula: ", matAlunos[cpfAlunos.index(cpf)],"\nNome: ", nomesAluno[cpfAlunos.index(cpf)], "\nCurso: ", cursoAlunos[cpfAlunos.index(cpf)],"\n")

def alterar_inscricao_mat(matAlunos):
    mat = input("Digite o código da matrícula: ").lower()
    while mat not in matAlunos:
        print("Essa matrícula não está na nossa base de dados. Tente novamente.")
        mat = input("Digite o código da matrícula: ").lower()

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

    if estado in capitais and len(capitaisAlunos)!=0: #inclusao
         capitaisAlunos[matAlunos.index(mat)]=capitais[capitais.index(estado)+1] #inclusao

    print("Os dados foram alterados com sucesso!\nMatrícula: ", matAlunos[matAlunos.index(mat)],"\nNome: ", nomesAluno[matAlunos.index(mat)], "\nCurso: ", cursoAlunos[matAlunos.index(mat)],"\n")

def listar_inscricoes():
    print(60*"-", "A01 – AI e Machine Learning", 60*"-", sep='\n')
    cadastrado = 0
    for index, item in enumerate(cursoAlunos):
        if item == "A01":
            cadastrado += 1
            print(f"{matAlunos[index]} – {nomesAluno[index]} - {capitaisAlunos[index]}")
    print(60*"-", f"Total de inscritos: {cadastrado}", 60*"-", "A02 – Business Intelligence", 60*"-", sep='\n')
    cadastrado = 0
    for index, item in enumerate(cursoAlunos):
        if item == "A02":
            cadastrado += 1
            print(f"{matAlunos[index]} – {nomesAluno[index]} - {capitaisAlunos[index]}")
    print(60*"-", f"Total de inscritos: {cadastrado}", 60*"-", "A03 – Governança em TI", 60*"-", sep='\n')
    cadastrado = 0
    for index, item in enumerate(cursoAlunos):
        if item == "A03":
            cadastrado += 1
            print(f"{matAlunos[index]} – {nomesAluno[index]} - {capitaisAlunos[index]}")
    print(60*"-", f"Total de inscritos: {cadastrado}", 60*"-", "A04 – Programação Python", 60*"-", sep='\n')
    cadastrado = 0
    for index, item in enumerate(cursoAlunos):
        if item == "A04":
            cadastrado += 1
            print(f"{matAlunos[index]} – {nomesAluno[index]} - {capitaisAlunos[index]}")
    print(60*"-", f"Total de inscritos: {cadastrado}", 60*"-", "A05 – Programação JAVA", 60*"-",sep='\n')
    cadastrado = 0
    for index, item in enumerate(cursoAlunos):
        if item == "A05":
            cadastrado += 1
            print(f"{matAlunos[index]} – {nomesAluno[index]} - {capitaisAlunos[index]}")
    print(60*"-", f"\nTotal de inscritos: {cadastrado}")


def validar_cpf(cpf):
    validade = False
    cpf = ''.join(re.findall('\d', str(cpf)))
    novo = cpf[:9]

    # digito 1
    l1 = []
    for i, v in reversed(list(enumerate(reversed(novo)))):
        l1.append((i + 2) * int(v))
    resto = sum(l1) % 11

    if resto < 2:
        f = 0
    else:
        f = 11 - resto
    novo += str(f)

    # digito 2
    l2 = []
    for i, v in reversed(list(enumerate(reversed(novo)))):
        l2.append((i + 2) * int(v))
    resto = sum(l2) % 11

    if resto < 2:
        f = 0
    else:
        f = 11 - resto
    novo += str(f)

    if novo == '00000000000' or novo == '11111111111' or novo == '22222222222' or novo == '33333333333' or novo == '44444444444' or novo == '55555555555' or novo == '66666666666' or novo == '77777777777' or novo == '88888888888' or novo == '99999999999':
        print(" CPF inválido. Digite novamente")
    else:
        if cpf == novo:
            validade = True

        else:
            validade = False

    return validade


def validar_estado(input):
    if type(input) != str:
        print("Texto nao reconhecido, favor utilizar outro")
        return False
    regioes = getRegioes()
    for reg in regioes:
        for estados in reg:
            for element in estados:
                if(removerAcento(input).lower()==removerAcento(element).lower()):
                    return True
    return False


def remover_acento(texto):
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


def get_regioes():
    return [[("Amazonas", "AM", "Manaus"), ("Roraima", "RR"), ("Pará", "PA"), ("Amapá", "AP"), ("Tocantins", "TO"), ("Rondônia",
              "RO"), ("Acre", "AC")], [("Maranhão", "MA"), ("Piauí", "PI"), ("Ceará", "CE"), ("Rio Grande do Norte",
              "RN"), ("Pernambuco", "PE"), ("Paraíba", "PB"), ("Sergipe", "SE"), ("Alagoas", "AL"), ("Bahia", "BA")], [
              ("Mato Grosso", "MT"), ("Mato Grosso do Sul", "MS"), ("Goiás", "GO"), ("Distrito federal", "DF")], [("São"
              " Paulo", "SP"), ("Rio de Janeiro", "RJ"), ("Espírito Santo", "ES"), ("Minas Gerais", "MG")], [("Paraná",
              "PR"), ("Rio Grande do Sul", "RS"), ("Santa Catarina", "SC")]]


def mostrarCursos(estado):
    cod = []

    norte = ["AC", "AP", "AM", "PA", "RO", "RR", "TO"]
    nordeste = ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]
    centroOeste = ["GO", "MT", "MS", "DF"]
    sudeste = ["ES", "MG", "SP", "RJ"]
    sul = ["PR", "RS", "SC"]

    cursosNordeste = ['A01 - AI e Machine Learning', 'A02 - Business Intelligence']
    cursosSudeste = ['A01 - AI e Machine Learning', 'A04 - Programação Python', 'A05 - Programação JAVA']
    cursosSul = ['A01 - AI e Machine Learning', 'A04 - Programação Python']
    cursosNorte = ['A01 - AI e Machine Learning', 'A04 - Programação Python']
    cursosCentroOeste = ['A01 - AI e Machine Learning', 'A03 - Governança em TI']

    if estado.upper() in norte:
        for curso in cursosNorte:
            cod.append(curso[0:3])
            print(curso)
    elif estado.upper() in nordeste:
        for curso in cursosNordeste:
            cod.append(curso[0:3])
            print(curso)
    elif estado.upper() in centroOeste:
        for curso in cursosCentroOeste:
            cod.append(curso[0:3])
            print(curso)
    elif estado.upper() in sul:
        for curso in cursosSul:
            cod.append(curso[0:3])
            print(curso)
    elif estado.upper() in sudeste and estado.upper() != "RJ":
        for curso in cursosSudeste:
            cod.append(curso[0:3])
            print(curso)
    else:
        cursosSudeste.pop(2)
        for curso in cursosSudeste:
            cod.append(curso[0:3])
            print(curso)
    return(cod)
