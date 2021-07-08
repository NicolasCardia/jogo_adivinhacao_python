import random

def jogar():

    print("*******************************")
    print("bem vindo ao jogo de advinhação")
    print("*******************************")

    numero_secreto = random.randrange(1, 10)+1
    print(numero_secreto)
    total_tentativas = 0
    pontos = 10

    print("Qual o nível de dificuldade?")
    print("1()Fácil  2()Médio  3()Difícil", "\n")

    nivel = int(input("> "))

    if(nivel == 1):
        total_tentativas = 5
    elif(nivel == 2):
        total_tentativas = 3
    elif(nivel == 3):
        total_tentativas = 1
    else:
        print("escolha um nivel valido")


    for tentativa in range (1, total_tentativas +1):
        chute = int(input("Digite um palpite entre 1 a 10: "))

        print("tentativa {} de {}".format(tentativa, total_tentativas) )
        print("você digitou", chute)

        if(chute < 1 or chute > 10):
            print("número invalido, digite um número de 1 a 10", "\n")
            continue
        else:
            acertou = chute == numero_secreto 
            chute_maior = chute > numero_secreto
            chute_menor = chute < numero_secreto

            if (acertou):
                print("Parabéns! você acertou e fez {} pontos.".format(pontos), "\n")
                break
            else: 
                if( chute_maior ):
                    print("Você errou, O numero secreto é MENOR", "\n")
                elif( chute_menor ):
                    print("Você errou, O numero secreto é MAIOR", "\n")
                pontos_perdidos = 2
                pontos -= pontos_perdidos

    print('Fim do jogo.')

if(__name__ == "__main__"):
    jogar()
