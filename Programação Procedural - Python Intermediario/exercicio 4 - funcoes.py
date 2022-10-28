"""
4 - Fizz Buzz - Se o parametro da função for divisivel 3, retorne fizz, se o parametro da funcao for divisivel por 5, retorne buzz.
Caso o parametro seja divisivel por 5 e 3, retorne fizz buzz. Se não, retorne o número enviado
"""

def fizzbuzz(n1):
    if n1 % 3 ==0 and n1 % 5 ==0:
        return "fizz buzz"
    elif n1 % 3 == 0:
        return "fizz"
    elif n1 % 5 ==0:
        return "buzz"
    else:
        return n1

var = fizzbuzz(15)
print(var)
