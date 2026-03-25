# ## Exercícios

# numeros = [1, 4, 2, 7, 9]

# numeros_ordenado = sorted(numeros) # cria nova lista ordenada
# numeros.sort() # altera a lista original ordenando-a


# numeros.append(5)
# # print(numeros)

# nomes = ["Maria", "Pedro", "Mateus", "Maria"]
# print(nomes.count("Maria"))

# nomes_copia = nomes.copy()
# print(nomes_copia)

# nomes.insert(2, "Marcos")
# print(nomes)

# nomes.remove("Maria") # remove a primeira ocorrência do valor
# print(nomes)

# nomes.remove("Maria")
# print(nomes)

lista = [ 1, 2, 8, 4, 3, 7 ]
# print(lista[::])

copia_lista = lista[::]
# print(copia_lista)

lista.sort()

# print(lista)
# print(copia_lista)

copia_lista_2 = lista
# print(copia_lista_2)

lista.remove(8)
# print(lista)

# print(copia_lista_2)

print(lista[::])

# print(lista[1:4])
print(lista[1::2])