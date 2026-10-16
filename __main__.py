from bankaccount import *
from pwinput import pwinput 
from time import sleep

if __name__ == "__main__":
    print("=========================================")
    print("      SISTEMA CORE CAPIBA BANK v1.0      ")
    print("=========================================")

    while True:
        print("\n[ MENU INICIAL ]")
        print("1. Criar uma Conta")
        print("2. Acessar uma Conta Existente")
        print("3. Encerrar Sistema")
        
        opcao = input("Selecione uma opção: ").strip()
        
        match opcao:
            case "1":
                resultado_cadastro = criar_conta()
                if resultado_cadastro:
                    print(f"\n{resultado_cadastro}")
                    sleep(5)
            case "2":
                conta_logada = acessar_conta()
                
                if conta_logada is not None:
                    while True:
                        print(f"\n[ OPERAÇÕES DISPONÍVEIS - TITULAR: {conta_logada.get_titular()} ]")
                        print("1. Sacar")
                        print("2. Depositar")
                        print("3. Consultar Saldo")
                        print("4. Emitir Extrato")
                        print("5. Alterar Nome do Titular")
                        print("6. Logout (Sair da Conta)")   
                        
                        sub_opcao = input("Selecione a operação desejada: ").strip()
                        
                        if sub_opcao == "1":
                            try:
                                valor = float(input("Digite o valor do saque: R$ "))
                                senha = pwinput("Confirme sua senha de 6 dígitos: ").strip()
                                resultado = conta_logada.sacar(valor, senha)
                                print(f"\n👉 {resultado}")
                                sleep(5)
                            except ValueError:
                                print("\n❌ Erro: Digite um valor numérico válido para a operação.")
                
                        elif sub_opcao == "2":
                            try:
                                valor = float(input("Digite o valor do depósito: R$ "))
                                resultado = conta_logada.depositar(valor)
                                print(f"\n👉 {resultado}")
                                sleep(5)
                            except ValueError:
                                print("\n❌ Erro: Digite um valor numérico válido para a operação.")
                
                        elif sub_opcao == "3":
                            print(f"\n👉 {conta_logada.exibir_saldo()}")
                            sleep(5)
                            
                        elif sub_opcao == "4":
                            conta_logada.extrato()
                            sleep(5)
                            
                        elif sub_opcao == "5":
                            novo_nome = input("Digite o novo nome para o titular: ").strip()
                            senha = pwinput("Confirme sua senha de 6 dígitos para alteração cadastral: ").strip()
                            resultado = conta_logada.set_titular(novo_nome, senha)
                            print(f"\n👉 {resultado}")
                            sleep(5)
                            
                        elif sub_opcao == "6":
                            print(f"\n🔒 Sessão encerrada de forma segura para o titular {conta_logada.get_titular()}.")
                            break
                            
                        else:  
                            print("\n❌ Opção operacional inválida!")
                            
            case "3":
                print("\nDesligando servidores do Capiba Bank... Até logo!")
                break
            case _:
                print("\n❌ Opção inicial inválida!")
