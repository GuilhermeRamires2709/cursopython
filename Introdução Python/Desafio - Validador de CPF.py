"""
CPF = 168.995.350-09
___________________
Fórmula de cálculo

1*10=10         1*11
6*9=54          6*10
8*8=64          8*9
9*7=63          9*8
9*6=54          9*7
5*5=25          5*6=30
3*4=12          3*5=15
5*2=10          5*4=20
0*1=0           0*3=0
                Digito 1 * 2 = 0
Soma = 297      soma = 343
                calculo 2 = 11 - (343 % 11)
                se calculo 2 > 9 digito 1 = 0
calculo = 11-(soma % 11) = 11
se calculo > 9 digito 1 = 0


"""

cpf=input("Digite seu CPF (Apenas números por favor): ")

contador1 = 10
contador2 = 11
x=0
y=0
soma1=0
soma2=0
lista=[]
for n in cpf:
    if len(lista)>=9:
        break
    lista.append(n)
    x=int(n)*contador1
    contador1-=1
    soma1+=x

calculo1= (11-(soma1 % 11))
if calculo1>9:
    digito1=0
else:
    digito1= calculo1
lista.append(digito1)

lista=[]

for n in cpf:
    if len(lista)>=10:

        break
    lista.append(n)
    y = int(n) * contador2
    contador2 -= 1
    soma2 += y

calculo2 = (11 - (soma2 % 11))
if calculo2 > 9:
    digito2 = 0
else:
    digito2 = calculo2
lista.append(str(digito2))

cpf_validado=''.join(lista)

if cpf_validado == cpf:
    print("Seu CPF é verdadeiro")
else:
    print("CPF Inválido")
