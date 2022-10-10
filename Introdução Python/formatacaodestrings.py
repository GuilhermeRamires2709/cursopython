nome = "Guilherme"
idade=19
altura=1.75
e_maior=idade>18
peso=57
imc=peso/(altura**2)
print('Nome:', nome  )
print("Idade:", idade)
print("Altura:", altura)
print("É maior de idade:", e_maior)
print("{n} tem {i} anos e seu IMC é {im:.2f} ".format(n=nome, i=idade, im=imc))