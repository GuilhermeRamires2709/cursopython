"""
Criação de um jogo da forca
"""
palavra_secreta="namorada"
letras_digitadas=[]
chances=3
i=0

while chances > 0:
    letra=input("Digite uma letra")

    if len(letra)>1:
        print("Você digitou mais do que uma letra! Digite uma única letra: ")
        continue
    else:
        letras_digitadas.append(letra)
        contador=0
        if letra in palavra_secreta:
            print("Parabéns! A letra que você digitou faz parte da palavra secreta")
            variavel = ""
            for l in palavra_secreta:
                if l in letras_digitadas:
                    variavel += l
                else:
                    variavel +='-'
            if variavel == palavra_secreta:
                print(f"Você acertou! A palavra secreta era {palavra_secreta}")
                break
            else:
                print(f"A palavra secreta é {variavel}")
        else:
            if chances == 1:
                print("Você perdeu! Tente outra vez!")
                chances -=1
            else:
                chances -=1
                print(f"Continue tentando! Você ainda tem {chances} chances")
                letras_digitadas.pop()




