class Banco_Intel:
    def __init__(self , titular = "" , Id = 0 ,saldo = 0):
        self.titular = titular
        self.Id = Id
        self.saldo = saldo
        self._extrato = []
        self.limete = 3

    def depositar(self ,valor):
        if valor < 1:
            print("Não foi possivel fazer o deposito valor menor ou igual a R$1,00")
        else:
            self.saldo += valor
            print(f"Deposito de valor {valor:.2f} realizado com sucesso")
            self._extrato.append(f"Deposito : {valor:.2f}")

    def sacar(self , valor):
        if valor > self.saldo :
            print(f"Conta de ID {self.Id} Não tem saldo suficiente")
        elif valor > 500:
            print(f"Valor Maior que R$500,00")
        elif self.limete == 0:
            print("Limite Maximo de Saque diario atingido")
        else:
            self.limete -= 1
            self.saldo -= valor
            print(f"Saque de valor {valor:.2f} Realizado Com sucesso")
            self._extrato.append(f"SAQUE : {valor:.2f}")

    def extrato(self):
        print(self._extrato)

user_1 = Banco_Intel("Vitor Oliveira" , 9579907 , 10000)
user_1.depositar(500)
user_1.sacar(250)
user_1.depositar(1000)
user_1.extrato()
