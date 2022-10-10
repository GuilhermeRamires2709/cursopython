"""
* Criar variaveis para nome (str), idade (int), altura (float), peso(float) de uma pessoa
* Criar variavel com o ano atual(int)
* Obter o ano de nascimento de uma pessoa
* Obter o IMC com 2 casas decimais
* Exibir um texto com todos os valores na tela, utilizando F strings com as chaves{}

"""
nome="Nahara"
idade=18
altura=1.65
peso=65
ano=2022
anoNasc=2022-idade
imc=(peso/(altura**2))
print(f"{nome} tem {idade} anos, \n {altura} de altura \n pesa {peso} kg \n nasceu em {anoNasc} \n Tem {imc:.2f} de imc")

