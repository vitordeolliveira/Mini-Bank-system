from abc import ABC
from abc import abstractmethod
class Banco_Intel(ABC):
    def __init__(self , titular = "" , Id = 0 ,saldo = 0):
        self._titular = titular #Protect (+)
        self.Id = Id #Public (#)
        self.__saldo = saldo #Priveted (-)
        self._extrato = [] #Protect (+)
        self.limete = 3

    def depositar(self ,valor):
        valor = abs(valor)
        if valor < 1:
            return("Não foi possivel fazer o deposito valor menor que R$1,00")
        else:
            self.__saldo += valor
            self._extrato.append(f"Deposito : R${valor:.2f}")
            return(f"Deposito de valor R${valor:.2f} realizado com sucesso")
           

    def sacar(self , valor):
        valor = abs(valor)
        if valor > self.__saldo :
            return(f"Conta de ID {self.Id} Não tem saldo suficiente")
        elif valor > 500:
            return(f"Saque Inválido valor Maior que R$500,00")
        elif self.limete == 0:
            return("Limite Maximo de Saque diario atingido")
        else:
            self.limete -= 1
            self.__saldo -= valor
            self._extrato.append(f"SAQUE : R${valor:.2f}")
            return (f"Saque de valor R${valor:.2f} Realizado Com sucesso")

    def extrato(self):
        return(self._extrato)
    
    def saldo_da_conta(self):
        return (f"Conta de ID {self.Id} com saldo atua = R${self.__saldo:.2f} ")

user_1 = Banco_Intel("Vitor Oliveira" , 9579907 , 10_000)
print(user_1.depositar(500))
print(user_1.sacar(250))
print(user_1.depositar(1000))
print(user_1.extrato())
print(user_1.saldo_da_conta())
