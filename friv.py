import forca
import advinhacao

def escolha_jogo():
    print('-------------------------------------------')
    print('-------------Escolha o jogo----------------')
    print('-------------------------------------------')
    print('(1) - Forca')
    print('(2) - Adivinhação')
    escolha = int(input('Digite a opção desejada: '))
    if escolha == 1:
        forca.jogar()
    elif escolha == 2:
        advinhacao.jogar()
    else:
        print('Digite uma opção certa porra')

if(__name__=="__main__"):
    escolha_jogo()
