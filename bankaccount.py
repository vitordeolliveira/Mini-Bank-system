from models.capiba_bank import Capiba_Bank
from pwinput import pwinput

banco_de_dados_local = {}

def criar_conta():
    try:
        nome = input("Digite o nome do titular da conta: ").strip()
        id_conta = int(input(f"Digite o ID da conta do(a) {nome}: "))
        if id_conta in banco_de_dados_local:
            return "Erro: Já existe uma conta registrada com este ID!"
        saldo = float(input(f"Qual o saldo atual da conta de ID {id_conta}: "))
        senha = pwinput("Crie uma senha de 6 dígitos: ").strip()
        if len(senha) != 6:
            return "Erro: A senha precisa ter exatamente 6 dígitos!"    
        nova_conta = Capiba_Bank(nome, id_conta, saldo, senha)
        banco_de_dados_local[id_conta] = nova_conta
        return f"Conta do(a) {nome} criada com sucesso e registrada na memória!"
    except ValueError:
        return "Erro: Dados numéricos inválidos! Digite apenas números inteiros para o ID e decimais para o Saldo."

def acessar_conta():
    try:
        print("\n=== LOGIN NO CAPIBA BANK ===")
        id_busca = int(input("Digite o ID da conta: "))
        if id_busca not in banco_de_dados_local:
            print ("Erro: Nenhuma conta localizada com este ID!")
        conta_ativa = banco_de_dados_local[id_busca]
        senha_verificacao = pwinput("Digite sua senha de 6 dígitos: ").strip()
        if conta_ativa.validar_senha(senha_verificacao):
            return conta_ativa
        else:
            print ("Falha na autenticação: Senha incorreta!")
    except ValueError:
        print ("Erro: O ID inserido precisa ser um número inteiro.")
