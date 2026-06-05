# Sistema Bancário - Banco Intel 🏦

Um sistema bancário simples e eficiente desenvolvido em Python utilizando o paradigma de **Programação Orientada a Objetos (POO)**. O projeto simula operações financeiras básicas de uma conta corrente, como depósitos, saques e visualização de extrato, aplicando regras de negócio e limites diários.

## 🚀 Funcionalidades

* **Depósito Seguro**: Permite adicionar fundos à conta, validando um valor mínimo de R\$ 1,00 para a operação.
* **Saque Controlado**: Realiza saques verificando o saldo disponível e aplicando duas travas de segurança:
  * Limite máximo de **R\$ 500,00 por saque**.
  * Limite de **3 saques diários**.
* **Histórico de Extrato**: Armazena e exibe todas as movimentações financeiras realizadas na conta em uma lista.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**: Linguagem de programação principal.
* **Programação Orientada a Objetos (POO)**: Estruturação do código em classes para maior organização e reutilização.

## 📋 Como Funciona o Código

A classe principal `Banco_Intel` gerencia as seguintes propriedades de cada cliente:
* `titular`: Nome do dono da conta.
* `Id`: Identificador único do cliente.
* `saldo`: Valor em dinheiro disponível.
* `_extrato`: Lista privada que guarda o histórico de transações.
* `limete`: Contador que controla a quantidade de saques restantes.

### Exemplo de Uso

No final do arquivo, o código realiza o seguinte fluxo de teste:

```python
# Criando um usuário com saldo inicial
user_1 = Banco_Intel("Vitor Oliveira", 9579907, 10000)

# Executando operações
user_1.depositar(500)
user_1.sacar(250)
user_1.depositar(1000)

# Exibindo as movimentações salvas
user_1.extrato()
```

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Baixe ou copie o código do arquivo `main.py`.
3. Abra o terminal na pasta do arquivo e execute o comando:
   ```bash
   python main.py
   ```
