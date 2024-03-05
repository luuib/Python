import jogo_forca
import adivinhacao

def escolha_jogos():
    print("***********************")
    print("** Qual jogo vc que? **") 
    print("***********************")
    print("(1)Forca,(2)Adivinhacao")

jogo = int(input("escolha um jogo"))
if = (jogo == 1):
    print("Jogando forca")
    jogo_forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()