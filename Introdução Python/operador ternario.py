"""
Operador ternario em python
"""

logged_user = False

msg="Usuário logado" if logged_user else "Usuário invalido"

print(msg)

idade = int(input("Digite sua idade: "))
e_maior=(idade>=18)
msg="è maior" if e_maior else "è de menor"

print(msg)
