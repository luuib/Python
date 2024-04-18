
num1 = int(input("Escreva o um numero"))
num2 = int(input("Escreva o outro numero"))


opc = input("qual calculo vc quer: +, -, /, *")

if opc == '+':
    resultado = num1 + num2
elif opc == '-':
    resultado = num1 - num2
elif opc == '/':        
    resultado = num1 / num2
elif opc == '*':
    resultado = num1 * num2


if num2 == 0:
    print("Erro :nao tem como dividir")

print(f"O resultado da operaçao e {num1} {opc} {num2} é: {resultado}")

