import os
os.system("cls" if os.name == "nt" else "clear")

import random

def jogar():

    numero_secreto = random.randint(1,10)
    total_de_rodadas = 0
    pontos = 50

    print("*Bem vindo ao jogo*")
    print("")

    print("Qual o nivel de dificuldade?")
    print("(1) Facil / (2) Médio / (3) Dificil")
    nivel = int(input("Escolha o nível: "))
    print("")

    if(nivel == 1):
        total_de_rodadas = 6
    elif(nivel == 2):
        total_de_rodadas = 4
    else:
        total_de_rodadas = 2

    for rodada in range(1, total_de_rodadas + 1):
        print(f"Tentativa {rodada} de {total_de_rodadas}")
        chute = int(input("Digite um número de 1 a 10: "))

        if(chute < 1 or chute > 10):
            print("Você não digitou um número entre 1 e 10.")
            print("")
            continue

        acertou = (chute == numero_secreto)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if(acertou):
            print("")
            print(f"Você acertou! O número secreto era {numero_secreto}.")
            print(f"Você fez {pontos} pontos.")
            break
        else:
            if(maior):
                print(f"O número que você chutou é maior que o número secreto.")
            elif(menor):
                print(f"O número que você chutou é menor que o número secreto.")
            
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = (pontos - pontos_perdidos)
        print("")

        if(total_de_rodadas == rodada):
            print(f"Acabou as tentativas, o número secreto era {numero_secreto}.")
            print(f"Você fez {pontos} pontos.")

    print("")
    print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar()
    
    


