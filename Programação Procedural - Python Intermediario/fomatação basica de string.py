"""
Formatação básica de strings
s-string
d - int
f - float
. <número de digitos> f
x ou X - Hexadecimal
(Caractere)(<>^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal -+ ou -
Ex. : 0>-100,.1f
Conversion flags - !r !s !a

"""

variavel= 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{10000.56767:,.2f}')
print(f'O Hexadecimal de 1500 é {1500:08X}')
