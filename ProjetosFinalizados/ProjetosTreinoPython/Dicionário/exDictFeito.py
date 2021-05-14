


def recebe(ra):
    alunos = {8640:'ativo', 3330:'ativo', 2067:'inativo'}
    if ra in alunos:
        print(f"O aluno {ra} está {alunos.get(ra)}")
    else:
        print("Ra não presente no nosso banco de dados, lelek.")








RA = int(input("Informe o ra do aluno \n"))
recebe(RA)