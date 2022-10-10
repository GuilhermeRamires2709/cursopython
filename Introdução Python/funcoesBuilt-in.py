"""
#Checagem de variaveis

is decimal
is numeric
is digit
"""
num_1=input("Digite um número: ")
num_2=input("Digite outro número")

if num_1.isnumeric() and num_2.isnumeric():
    print(f"soma {num_1 + num_2} ")
else:
    print("invalido")

n_1=input("Digite o primeiro")
n_2=input("Digite o segundo")

try:
    n_1 = float(n_1)
    n_2 = float(n_2)
    print(n_1 + n_2)
except:
    print("ERROR")