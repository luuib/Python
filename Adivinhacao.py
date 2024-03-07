import forca
import advinhac

def escolJogo():
    print('Escolha o jogo')
    print('1 - Forca')
    print('2 - Adivinhação')
    escolha = int(input('Digite a opção desejada:'))
    if escolha == 1:
        forca.jogar()
    elif escolha == 2:
        advinhac.jogar()
    else:
        print('Digite uma opção certa macaco')

if(__name__=="__main__"):
    escolJogo()
