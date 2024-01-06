import forca
import adivinhacao

print("***Escolha o jogo!***")
print("")

print("(1) Forca / (2) Adivinhação")
jogo = int(input("Qual jogo? "))
print("")

if (jogo == 1):
    print("Jogando Forca!")
    forca.jogar()
elif (jogo == 2):
    print("Jogando Adivinhação!")
    adivinhacao.jogar()
