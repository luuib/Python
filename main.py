#nome=input("Escreva o seu nome")
#idade=input ("Escreva a sua idade")
#idade=int(idade)
#print(f"Olá, {nome}, voce tem {idade} anos")
#try:
 #   idade=int(input("Escreva a sua idade"))
#except ValueError:
 #       print("voce nao digitou a sua idade")
 
 num1 = input ("escreva um numero de 0 a 9")
 
 num2 = input("escreva um numero de 10 a 20")
 
    try:
        num1 =float(input("escreva um numero"))
        operador= input("Escreva  o operador(+,-):")
        num2 = float(input("Escreva outro numero"))
        
        except ValueError:
            print("tente novamente")
            
            soma = num1 + num2
                
                print(f"(O numero {num1} mais o numero {num2} é igual a: {soma}."))
                
