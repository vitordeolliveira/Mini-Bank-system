from core.bank import Bank

class Capiba_bank(Bank):
    def __init__(self, titular, Id, saldo, chave):
        super().__init__(titular, Id, saldo, chave)

    def extrato(self):
        print(f"=== EXTRATO CONSOLIDADO - CONTA ID {self.Id} ===")
        if len(self._extrato) == 0:
            print("Nenhuma transação realizada até o momento.")
        else:
            for transacao in self._extrato:
                print(transacao)


    def exibir_saldo(self):
        return f"Saldo atual da conta de ID{self.Id} = R${super().get_saldo():.2f}"