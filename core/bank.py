from abc import ABC, abstractmethod
from hashlib import sha256


class Bank(ABC):
    def __init__(self , titular:str , Id:int, saldo:float, chave:str):
        self._titular = titular 
        self.Id = Id 
        self._saldo = saldo
        self._extrato = []
        self._hash = sha256(chave.encode('utf-8')).hexdigest() 
        self.limite_max = 1000

    def validar_senha(self , chave:str) -> bool:
        user = sha256(chave.encode('utf-8')).hexdigest()
        if user == self._hash:
            return True
        else:
            return False
    
    def get_saldo(self):
        return(self._saldo)

    def get_titular(self):
        return(self._titular)

    def set_titular(self, novo_titular, chave):
        if self.validar_senha(chave):
            if len(novo_titular.strip()) < 5:
                return "Erro: Nome inválido."
            self._titular = novo_titular
        else:
            return "Falha na autenticação, Alterações canceladas!"

    def depositar(self ,valor):
        if (valor < 1): 
            return "Não foi possível fazer o depósito, pois o valor é inferior a R$1,00"
        else:
            self._saldo += valor
            self._extrato.append(f"Depósito : R${valor:.2f}")
            return f"Depósito de valor R${valor:.2f} realizado com sucesso!"
               
    def sacar(self , valor, chave):
        if self.validar_senha(chave):
            if (valor > 500) or (valor < 1):
                return f"Saque Inválido valor superior a R$500,00 ou inferior a R$1,00"
            elif valor > self.limite_max:
                return "Saque não permitido, Limite Máximo de Saque diário(R$1,000.00) atingido"
            elif (valor > self._saldo) :
                return f"Conta de ID {self.Id} Não tem saldo suficiente!" 
            else:
                self.limite_max -= valor
                self._saldo -= valor
                self._extrato.append(f"SAQUE : R${valor:.2f}")
                return f"Saque de valor R${valor:.2f} Realizado Com sucesso"
        else:
            return"Falha na autenticação, Saque não autorizado!"

    @abstractmethod
    def extrato(self):
        pass

    @abstractmethod
    def exibir_saldo(self):
        pass
