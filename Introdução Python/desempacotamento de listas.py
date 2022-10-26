"""
Desempacotamento de listas em python

"""

lista = ['João', "José", "Maria", 1 ,2, 3]

n1,n2, n3, *_ = lista
 # "*_" serve para que outros desenvolvedores saibam que o restante da lista não vai ser utilizado

print(n1, n2, n3)