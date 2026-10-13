from abc import ABC

class Capiba_Bank(ABC):
    def __init__(self , titular = "" , Id = 0 ,saldo = 0):
        self._titular = titular #Protect (+)
        self.Id = Id #Public (#)
        self.__saldo = saldo #Priveted (-)
        self._extrato = [] #Protect (+)
        self.limite = 3

    def depositar(self ,valor):
        if valor < 1:
            return("Não foi possível fazer o deposito valor inferior a R$1,00")
        else:
            self.__saldo += valor
            self._extrato.append(f"Deposito : R${valor:.2f}")
            return(f"Deposito de valor R${valor:.2f} realizado com sucesso")
        
    def sacar(self , valor):
        if valor < 1:
            return("Não foi possível fazer o saque valor inferior a R$1,00")
        elif valor > self.__saldo :
            return(f"Conta de ID {self.Id} Não tem saldo suficiente")
        elif valor > 500:
            return(f"Saque Inválido valor superior a R$500,00")
        elif self.limite == 0:
            return("Limite Máximo de Saque diario atingido")
        else:
            self.limite -= 1
            self.__saldo -= valor
            self._extrato.append(f"SAQUE : R${valor:.2f}")
            return (f"Saque de valor R${valor:.2f} Realizado Com sucesso")

    def extrato(self):
        return(self._extrato)
    
    def saldo_da_conta(self):
        return (f"Conta de ID {self.Id} com saldo atual = R${self.__saldo:.2f} ")