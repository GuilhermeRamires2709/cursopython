"""
For in em Python
Iterando Strings com for
Função range (start=0, stop, step=1)

"""

texto = "Python"

c=0

"""for letra in texto:
    print(letra)"""


for n in range(20,10,-1):
    print(n)

#Função que avalia os multiplos de 8 de 0 até 100
for n in range(100):
    if n % 8==0:
        print(n)


texto="python"
nova_string=""

print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
for letra in texto:
    if letra =="t":
        nova_string=nova_string + letra.upper()
    elif letra=="h":
        nova_string+=letra.upper()
    else:
        nova_string+=letra

print(nova_string)


#Break - Quebra/Sai do Laço
#Continue - Pula para o próximo
print("3333333333333333333333")
nova=""
for letra in texto:
    if letra =="t":
        continue #não inclui a letra T, pula para  a próxima

    elif letra=="h":
        nova+=letra.upper()
    else:
        nova+=letra

print(nova)