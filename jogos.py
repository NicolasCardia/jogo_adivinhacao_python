import forca
import adivinhacao

def escolhe_jogo():
    print("*******************************")
    print("        escolha um jogo       ")
    print("*******************************")

    print("(1) forca  (2) Adivinhação")
    jogo = int(input("Escolha o jogo que deseja jogar: "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando adivinhação")
        adivinhacao.jogar()
    else:
        print("Esse jogo não existe!")

if(__name__ == "__main__"):
    escolhe_jogo()