import random

def jogar_jokenpo(): 
    opcoes = ["pedra","papel","tesoura"]
    vitorias = 0
    print("Bora jogar jokenpo")
    print("qual vc escolhe:pedra, papel, tesoura")



    while True:
        escolha_jogador = input("Sua escolha:")
        if escolha_jogador not in opcoes:
            print("escolhe invaleda,Tenta denovo ")
            continue 
        
        escolha_pc = random.choice(opcoes)

        print(f"O Pc escolheu:{escolha_pc}.")

        resultado = vencedor(escolha_jogador, escolha_pc)
        print(resultado)

        if resultado == "Vocẽ ganhou":
            vitorias +=1
        elif resultado == "voce perdeu":
            vitorias -= 1
        else:
            vitorias += 0

        print(f"Total de vitorias: {vitorias}")

        jogar_novamente = input("Bora mais uma?").lower()
        if jogar_novamente !="sim":
            break

def vencedor(escolha_jogador,escolha_pc):
    if escolha_jogador  == escolha_pc:
            return "Deu empate"
    elif (
        (escolha_jogador == "papel" and escolha_pc == "pedra")or
        (escolha_jogador == "pedra" and escolha_pc == "tesoura")or
        (escolha_jogador == "tesoura" and escolha_pc == "papel")
    ):
        return "Vocẽ ganhou"
    else:
        return "voce perdeu"



if __name__ == "__main__":
    jogar_jokenpo()