# def mostrarCursos(estado):
#
#     norte = ["AC", "AP", "AM", "PA", "RO", "RR", "TO"]
#     nordeste = ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]
#     centroOeste = ["GO", "MT", "MS", "DF"]
#     sudeste = ["ES", "MG", "SP", "RJ"]
#     sul = ["PR", "RS", "SC"]
#
#     cursosNordeste = ['A01 - AI e Machine Learning',
#                       'A02 - Business Intelligence']
#     cursosSudeste = ['A01 - AI e Machine Learning',
#                     'A04 - Programação Python', 'A05 - Programação JAVA']
#     cursosSul = ['A01 - AI e Machine Learning', 'A04 - Programação Python']
#     cursosNorte = ['A01 - AI e Machine Learning', 'A04 - Programação Python']
#     cursosCentroOeste = [
#         'A01 - AI e Machine Learning', 'A03 - Governança em TI']
#
#     if estado.upper in norte:
#         for curso in cursosNorte:
#             print(curso)
#     elif estado.upper in nordeste:
#         for curso in cursosNordeste:
#             print(curso)
#     elif estado.upper in centroOeste:
#         for curso in cursosCentroOeste:
#             print(curso)
#     elif estado.upper in sul:
#         for curso in cursosSul:
#             print(curso)
#     elif estado.upper in sudeste and estado.upper != "RJ":
#         for curso in cursosSudeste:
#             print(curso)
#     else:
#         cursosSudeste.pop()
#         for curso in cursosSudeste:
#             print(curso)


def mostrarCursos(estado):
    cod=[]

    norte = ["AC", "AP", "AM", "PA", "RO", "RR", "TO"]
    nordeste = ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]
    centroOeste = ["GO", "MT", "MS", "DF"]
    sudeste = ["ES", "MG", "SP", "RJ"]
    sul = ["PR", "RS", "SC"]

    cursosNordeste = ['A01 - AI e Machine Learning',
                      'A02 - Business Intelligence']
    cursosSudeste = ['A01 - AI e Machine Learning',
                    'A04 - Programação Python', 'A05 - Programação JAVA']
    cursosSul = ['A01 - AI e Machine Learning', 'A04 - Programação Python']
    cursosNorte = ['A01 - AI e Machine Learning', 'A04 - Programação Python']
    cursosCentroOeste = [
        'A01 - AI e Machine Learning', 'A03 - Governança em TI']

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
