"""
Fazer um programa onde o usuário digita um número inteiro, verifica se é par ou ímpar e retorna.
Caso não seja informado um inteiro, o programa deve retornar o erro


num=input("Digite um número inteiro")

if num.isnumeric():
    num=int(num)
    d=num/2;
    if d.is_integer():
        print(f"O número {num} é par")
    else:
        print(f"O número {num} é ímpar")
else:
    print(f"{num} não é um número do tipo inteiro inteiro")
"""
"""
Receber a hora e retornar a saudação ao usuário de acordo com a hora. Ex: Bom dia, fulano!
"""

hora=input("Digite a hora atual (0-23)")

if hora.isdigit():
    hora=int(hora)
    if hora > 0 and hora <=12:
        print("Bom dia")
    elif hora > 12 and hora <=18:
        print("Boa tarde")
    else:
        print("Boa noite")

"""
Receber o nome do usuário e verificar o num de letras, após retornar "muito pequeno" se <= 4, 
"Normal" 4>=<6 e "Muito Grande se maior"

#Aqui inicia o código
nome=input("Digite seu nome")

if nome.isascii():
    if len(nome) <= 4:
        print(f"{nome} é um nome curto")
        
    elif len(nome) > 4 and len(nome) <= 6:

        print(f"{nome} é um nome de tamanho normal")
    else:
        print(f"{nome} é um nome muito longo")

#Aqui finaliza o código

"""