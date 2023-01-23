"""
#ADD (adiciona) update(atualiza), clear, discard
#union | (une)
# intersection & (todos os elementos presentes nos dois sets)
#difference - (elementos apenas no set da esquerda)
#symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""

s1 = set()
s1.update([1,2,3,4,5], {5,6,7,8})

print(s1)

#Sets não permitem repetição de item, portanto podem ser utilizados para eliminar elementos duplicados de uma lista.
#PS: Isso pode desordenar a lista

l1=[1,2,3,3,3,3,4,4,5,6,7,'Guilherme', 'Guilherme']
l1=set(l1)
print(l1)

#União entre conjuntos
print("Union:")
set_1={1,2,3,4,5}
set_2={1,2,3,4,5,6,7}
set_3= set_1 | set_2
print(set_3)
#set_3 pega todos os elementos diferentes
print("Difference:")
set_10={1,2,3,4,5}
set_20={1,2,3,4,5,6,7}
set_30=  set_20 - set_10
print(set_30)
#set_3 Pega todos os elementos diferentes apenas no conjunto da ESQUERDA


list1 = {"João", "Maria", "José"}
list2 = {"Maria", "José", "João", "João", "Maria", "José"}

#Forma de verificar se são os mesmos elementos presentes em ambas as listas
if set(list1) == set(list2):
    print("Lista 1 é igual lista 2")
else:
    print("São diferentes")

#Interseção

s2={1,3,6,9}
s3={1,2,3,4,5,6,7,8,9}
s4 = s2 & s3

print("Intersection")
print(s4)

#Symetric Difference

s5 = s2 ^ s3
print("Symetric")
print(s5)
