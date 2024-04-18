

num1 = int(input("Escreva o primeiro numero"))
num2 = int(input("Escreva o segundo numero"))



def escolher():
    while True:
        print("1-soma")
        print("2-subtraçao")
        print("3-divisao")
        print("4-multiplicaçao")
        print("5-sair")

        opc = input("qual calculo vc quer?")

        if opc == '1':
            resultado = num1 + num2
        elif opc == '2':
            resultado = num1 - num2
        elif opc == '3':        
            resultado = num1 / num2
        elif opc == '4':
            resultado = num1 * num2
        elif opc == '5':
            print("Adeus ...")
            break
        else:
            print("È pra escolher uma dessas 5 opcoes")

if __name__ == "__main__":
    escolher()