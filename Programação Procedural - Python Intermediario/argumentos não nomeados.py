"""
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembre-te de desempacotamento

def soma(*args):
    total=0
    for numero in args:
        print('Total', total, numero)
        total = total + numero
        print('Total', total)



soma( 1, 2 ,3, 4, 5, 6)