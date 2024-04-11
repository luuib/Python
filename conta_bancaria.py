class contaBancaria:
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor

    def exibir_detalhes(self):
        print("Numero da conta:", self.numero)
        print("Titular", self.titular)
        print("Saldo:", self.saldo)


    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("O seu saldo inuficiente")
        


#aqui crio uma instancia do objeto contaBancaris
#como nome conta_do_luiz

numero_conta = input("Digite o numero da conta")
titular_conta = input("Digite o titular da conta")
saldo_inicial = float(input("Digite o saldo inicial da conta:"))

conta_do_luiz = contaBancaria(numero_conta, titular_conta , saldo_inicial)

#Usando os metodos do objeto contaBancaria 

valor_depositar = float(input("digite o valor que sera depositado").replace(",","."))
valor_saque = float(input("digite o valor que sera sacado"))


conta_do_luiz.depositar(valor_depositar)
conta_do_luiz.sacar(valor_saque)
conta_do_luiz.exibir_detalhes()
