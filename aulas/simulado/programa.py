from funcoes import busca_plataforma, combina_dados, recomendacao

minhas_series = [
    {
        "plataforma": "Netflix",
        "titulo": "Stranger Things",
        "genero": "Ficção Científica"
    },
    {
        "plataforma": "HBO Max",
        "titulo": "Succession",
        "genero": "Drama"
    },
    {
        "plataforma": "Disney+",
        "titulo": "The Mandalorian",
        "genero": "Aventura"
    },
    {
        "plataforma": "Amazon Prime Video",
        "titulo": "The Boys",
        "genero": "Ação"
    },
    {
        "plataforma": "Apple TV+",
        "titulo": "Ted Lasso",
        "genero": "Comédia"
    }
]

plataformas = ["Netflix", "HBO Max", "Disney+", "Amazon Prime Video", "Apple TV+"]
titulos = ["Stranger Things", "Succession", "The Mandalorian", "The Boys", "Ted Lasso"]
genero = ["Ficção Científica", "Drama", "Aventura", "Ação", "Comédia"]


lista_series = [
    {"plataforma": "Netflix", "titulo": "Stranger Things", "genero": "Ficção científica"},
    {"plataforma": "Apple TV+", "titulo": "Ted Lasso", "genero": "Comédia"},
    {"plataforma": "Prime Video", "titulo": "The Boys", "genero": "Super-heróis"},
    {"plataforma": "Disney+", "titulo": "The Mandalorian", "genero": "Ficção científica"},
    {"plataforma": "HBO Max", "titulo": "Game of Thrones", "genero": "Fantasia"},
    {"plataforma": "Prime Video", "titulo": "The Marvelous Mrs. Maisel", "genero": "Comédia"},
    {"plataforma": "HBO Max", "titulo": "Friends", "genero": "Comédia"},
    {"plataforma": "Netflix", "titulo": "The Witcher", "genero": "Fantasia"},
    {"plataforma": "Prime Video", "titulo": "Fleabag", "genero": "Comédia"}
]

# print(len(plataformas))
# print(busca_plataforma("The Boys", minhas_series))

# print(combina_dados(plataformas, titulos, genero))

print(recomendacao("Ted Lasso", lista_series))