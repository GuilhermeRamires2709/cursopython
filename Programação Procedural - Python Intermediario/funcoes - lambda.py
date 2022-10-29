"""
Funções anonimas
"""

a = lambda x,y:  x * y

print(a(1,2))

#função simples para ordenar uma lista de produtos

lista = [
    ["P1", 10],
    ["P2", 12],
    ["P3", 7],
    ["P4", 5],
    ["P5", 11]
]

lista.sort(key=lambda item: item[1])
print(lista)

#Função para ordenar sem alterar a lista (apenas exibição)

lista = [
    ["P1", 10],
    ["P2", 12],
    ["P3", 7],
    ["P4", 5],
    ["P5", 11]
]
print(sorted(lista, key=lambda i: i[1]))
print(lista)