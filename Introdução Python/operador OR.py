"""
Operador or
"""

nome=input("Digite seu nome: ")

print(nome or "Vazio")


#Verifica se algum valor é verdadeiro

a=0
b=None
c=False
d=[]
e={}
f=22
g="Luiz"

variavel = a or b or c or d or e or f or g

print(variavel)