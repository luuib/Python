import random

def jogar_jokenpo(): 
    opcoes = ["pedra","papel","tesoura"]
    print("Bora jogar jokenpo")
    print("qual vc escolhe:pedra, papel, tesoura")

    while True:
        escolha_jogador = input("Sua escolha:")
        if escolha_jogador not in opcoes:
            print("escolhe invaleda,Tenta denovo ")
            continue 
        
        escolha_pc = random.choice(opcoes)

        print(f"O Pc escolheu:{escolha_pc}.")

        if escolha_jogador  == escolha_pc:
            print("Deu empate")
        elif (
            (escolha_jogador == "papel" and escolha_pc == "pedra")or
            (escolha_jogador == "pedra" and escolha_pc == "tesoura")or
            (escolha_jogador == "tesoura" and escolha_pc == "papel")
        ):
            print("Vocẽ ganhou")
        else:
            print("voce perdeu")

        jogar_novamente = input("Bora mais uma?").lower()
        if jogar_novamente !="sim":
            break

if __name__ == "__main__":
    jogar_jokenpo()