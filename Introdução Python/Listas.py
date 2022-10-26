"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend +
min, max
range
"""

l1 = [1,2,3]
l2= [4,5,6]
l3=l1+l2
print(l3)

#Adicionado ao final da lista

l1.append("B")

#Adicionando a um indice especifico

l2.insert(0,"banana")

print(l2)

#Remove o último caractere

l2.pop()
print(l2)

#Remove um índice especifico

del(l2[0])
print(l2)

#Cria uma lista
l2=list(range(1,10))
print(l2)
soma=0
for valor in l2:
    soma=soma+valor
    print(soma)

