d1 = {
    "Nome": "Guilherme",
    "Telefone": "051998164196",
    "Pai": "Anderson"
}
#Verificando se uma chave existe
print( 'str' in d1)
print( 'str' in d1.keys())
print( 'str' in d1.values())


#Manipulando/Iterando

for v in d1.items():
    print(v)


#

clientes={
    "Cliente1": {
        "Nome": "Guilherme",
        "Sobrenome": "Ramires"
    }, "Cliente2":{
        "Nome": "Douglas",
        "Sobrenome": "Vinicius"
    }
}

for clientes_1, clientes_2 in clientes.items():
    print(f"Exibindo {clientes_1}")
    for nome, sobrenome in clientes_2.items():
        print(f"{nome} = {sobrenome}")

#dicionario.pop("Chave") elimina uma chave e seu atributo/valor
#dicionario.popitem() elimina a ultima chave chave e seu atributo/valor

