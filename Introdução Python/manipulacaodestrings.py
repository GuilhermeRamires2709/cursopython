"""
manipulando strings - aula 6

* Strings indices
* Fatiamento de strings {inicio:fim:passo]
* Funções Built In len, abs, type, print e etc
"""
#positivos  [012345]
texto      ="python"

print(texto[2])

#negativos -[654321]
nova_string="python"
print(texto[2:6])

#Nesse caso ele vai percorrer do caracter 0 até 0 6 pulando de 2 em 2 caracteres
print(nova_string[0:6:2])

#Para saber o número de caracteres que uma string tem
print(len(texto))