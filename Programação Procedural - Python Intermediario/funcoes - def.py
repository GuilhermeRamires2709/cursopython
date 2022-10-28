"""
Funções - def em python
"""

def saudacao(msg='Olá', nome='Ze'):
    nome=nome.replace('e','3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'

variavel = saudacao()

print(variavel)

#Aula 2 - def

def divisao(n1, n2):
    if n2 ==0:
        return
    return (n1/n2)

divide = divisao(8,2)

if divide:
    print(divide)
else:
    print('Divisor inválido')

