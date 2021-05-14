from unicodedata import normalize

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
def removerAcento(texto):
    return normalize('NFKD', texto).encode('ASCII','ignore').decode('ASCII')
def getRegioes():
    return [
        [
            ("Amazonas" , "AM" )
            ,("Roraima" , "RR" )
            ,("Pará" , "PA" )
            ,("Amapá" , "AP" )
            ,("Tocantins" , "TO" )
            ,("Rondônia" , "RO" )
            ,("Acre" , "AC" )
        ],
        [
            ("Maranhão" , "MA" )
            ,("Piauí" , "PI" )
            ,("Ceará" , "CE" )
            ,("Rio Grande do Norte" , "RN" )
            ,("Pernambuco" , "PE" )
            ,("Paraíba" , "PB" )
            ,("Sergipe" , "SE" )
            ,("Alagoas" , "AL" )
            ,("Bahia" , "BA" )
        ],
        [
            ("Mato Grosso" , "MT" )
            ,("Mato Grosso do Sul" , "MS" )
            ,("Goiás" , "GO" )
            ,("Distrito federal","DF")
        ],
        [
            ("São Paulo" , "SP" )
            ,("Rio de Janeiro" , "RJ" )
            ,("Espírito Santo" , "ES" )
            ,("Minas Gerais" , "MG" )
        ],
        [ 
            ("Paraná" , "PR"),
            ("Rio Grande do Sul" , "RS" ),
            ("Santa Catarina" , "SC")
        ]
    ]

