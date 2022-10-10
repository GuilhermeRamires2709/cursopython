"""
Formatando valor com modificadores

:s - Texto
:d - Inteiro
:f - Float
:.(f) - num de casas decimais
: (Caractere) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

"""
nome="Ramires"
nome_formatado = '{n:#>10}'.format(n=nome)
print(nome_formatado)