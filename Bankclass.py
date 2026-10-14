from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self , titular = "" , Id = 0 ,saldo = 0):
        self._titular = titular 
        self.Id = Id 
        self._saldo = saldo
        self._extrato = [] 
        self.limite_max = 1000

    def get_saldo(self):
        return(self._saldo)

    def get_titular(self):
        return(self._titular)

    def set_titular(self, novo_titular):
        if len(novo_titular.strip()) < 3:
            print("Erro: Nome inválido.")
            return
        self._titular = novo_titular

    def depositar(self ,valor):
        if (valor < 1): 
            return("Não foi possível fazer o deposito valor inferior a R$1,00")
        else:
            self._saldo += valor
            self._extrato.append(f"Deposito : R${valor:.2f}")
            return(f"Deposito de valor R${valor:.2f} realizado com sucesso!")
               
    def sacar(self , valor):
        if (valor > 500) or (valor < 1):
            return(f"Saque Inválido valor superior a R$500,00 ou inferior a R$1,00")
        elif valor > self.limite_max:
            return("Saque não permitido, Limite Máximo de Saque diario(R$1,000.00) atingido")
        elif (valor > self._saldo) :
            return(f"Conta de ID {self.Id} Não tem saldo suficiente!")
        else:
            self.limite_max -= valor
            self._saldo -= valor
            self._extrato.append(f"SAQUE : R${valor:.2f}")
            return (f"Saque de valor R${valor:.2f} Realizado Com sucesso")
    @abstractmethod
    def extrato(self):
        pass
    @abstractmethod
    def exibir_saldo(self):
        pass