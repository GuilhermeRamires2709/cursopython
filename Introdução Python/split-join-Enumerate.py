"""
Split, Join, Enumerate em Python
* Split - Dividir uma String #str
* Join - Juntar uma lista #str
* Enumerate - Enumerar elementos da lista #list / iteraveis
"""

#Split
string = "O Brasil é o país do Brasil, o Brasil é penta"
lista1=string.split(" ")
lista2 = string.split(",")

palavra=''
contagem=0

for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor


print(f'A palavra que apareceu mais vezes é {palavra} que apareceu {contagem}x')

#Join
frase="O Brasil é penta"
lista=frase.split(' ')
frase2= ' '.join(lista)

print(f"Lista é {frase2}")

#Enumerate - Desempacotar listas

list = ["João", "José", "Joaquim"]

for indice, nome in enumerate(list):
    print(indice, nome)