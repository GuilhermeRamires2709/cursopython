"""
    Operadores relacionais + IF, Elif e Else
    ==, > , <, =>, <=, !=
"""

nome=input("Qual o seu nome? ")
idade=int(input("Qual a sua idade? "))

#Idade limite para pegar o empréstimo
idade_limite=18

if idade>=idade_limite:
    print(f"{nome} pode pegar um empréstimo")
else:
    print(f"{nome} NÃO pode pegar empréstimo")