"""
For / Else em Python
"""

variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith("j"):
        print(f"{valor} começa com J")
        break
else:
    print("Não existe valor que começa com J")