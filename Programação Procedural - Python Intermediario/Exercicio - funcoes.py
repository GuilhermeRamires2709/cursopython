"""
Exercicios com funções

Exercicio 1:

Criar uma função que multiplique todos os argumentos não nomeados recebidos e depois retornar o resultado
em uma variavel e exibir na tela

"""

def multiplicacao(*args):
    total=0
    for n in args:
        total = total * n
    return total

print(f"O resultado é: {total}")
