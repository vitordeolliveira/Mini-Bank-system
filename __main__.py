from Bankclass import *

def main():
    user_1 = Bank("Vitor Oliveira" , 9579907 , 10_000)
    print(user_1.depositar(500))
    print(user_1.sacar(500))
    print(user_1.depositar(1000))
    print(user_1.sacar(500))
    print(user_1.extrato())
    print(user_1.sacar(100))
    print(user_1.saldo_da_conta())

if __name__ == "__main__":
    main()

