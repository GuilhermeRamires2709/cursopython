"""
Exercicios com funções

Exercicio 1:

Criar uma função que multiplique todos os argumentos não nomeados recebidos e depois retornar o resultado
em uma variavel e exibir na tela

"""

def multiplicar(*args):
    total = 1
    for n in args:
        total *= n
    return total

multiplicacao=multiplicar(3,2,3)
print(multiplicacao)


"""
Crie uma função que fala se um número é par ou impar.
Retorne se o número é par
"""


def ver(n):
    calc = n % 2
    if calc == 0:
        return "par"
    else:
        return "impar"

numero=int(input("Digite"))
verificar=ver(numero)
print(verificar)