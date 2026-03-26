from typing import List

def busca_plataforma(titulo:str, lista_series:List[dict])->str:
    for serie in lista_series:
        if serie["titulo"] == titulo:
            return serie["plataforma"]


def combina_dados(plataformas:List[str], titulos:List[str], generos:List[str])->List[dict]:
    lista_series = []
    for i in range(len(plataformas)):
        lista_series.append({"plataforma":plataformas[i], "titulo":titulos[i], "genero":generos[i]})
    return lista_series

def recomendacao(titulo:str, lista_series:List[dict])->dict:
    genero = ""
    plataforma = ""
    for serie in lista_series:
        if serie["titulo"] == titulo:
            genero = serie["genero"]
            plataforma = serie["plataforma"]

    dic_recomendaco = {}
    for serie in lista_series:
        if serie["genero"] == genero:
            dic_recomendaco[serie["plataforma"]] = []
    
    for serie in lista_series:
        if serie["genero"] == genero and serie['titulo']!=titulo:
            dic_recomendaco[serie["plataforma"]].append(serie["titulo"])
    
    if dic_recomendaco[plataforma] == []:
        dic_recomendaco.pop(plataforma)
    
    return dic_recomendaco



# lista = ["cachorro","gato", "coelho"]
# # print(lista[1])

# serie = {"plataforma":"Netflix", "titulo":"Stranger Things", "genero":"Ficção"}
# # print(serie["plataforma"])
# print(serie["titulo"])

# cachorro = [ 1, 2, 3 ] 

# soma = 0

# for i in cachorro:
#     soma += i
# print(soma)