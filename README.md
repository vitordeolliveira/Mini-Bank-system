# Capiba Bank — Sistema Bancário em Python

Sistema bancário desenvolvido em Python com foco em Programação Orientada a Objetos (POO), utilizando herança, classes abstratas, encapsulamento e validação de operações.

O projeto implementa um fluxo bancário via terminal, permitindo criar contas, autenticar usuários e realizar operações básicas de movimentação e consulta de saldo.

## Funcionalidades

- **Criação de contas:** cadastro de titular, identificador, saldo inicial e senha.
- **Autenticação:** acesso à conta mediante ID e validação de senha.
- **Depósitos:** movimentação de saldo com validação do valor mínimo.
- **Saques:** validação de senha, saldo disponível, valor da operação e limite de saque.
- **Consulta de saldo:** exibição do saldo atual da conta.
- **Extrato:** registro e consulta das movimentações realizadas.
- **Alteração cadastral:** atualização do nome do titular mediante autenticação.
- **Gerenciamento de sessão:** acesso às operações da conta e encerramento da sessão.

## Tecnologias utilizadas

- **Python 3** — implementação da lógica e das regras de negócio.
- **Programação Orientada a Objetos** — organização do sistema em classes, com herança e abstração.
- **ABC (Abstract Base Classes)** — definição de uma classe base abstrata.
- **hashlib (SHA-256)** — geração de hash para validação de senhas.
- **pwinput** — entrada de senhas sem exibição dos caracteres no terminal.

## Conceitos aplicados

### Programação Orientada a Objetos

- **Abstração:** a classe `Bank` define uma estrutura comum para contas bancárias e declara métodos abstratos para exibição de saldo e extrato.
- **Herança:** `Capiba_Bank` herda os atributos e comportamentos de `Bank`, especializando as operações de apresentação.
- **Encapsulamento:** atributos como `_saldo`, `_titular`, `_extrato` e `_hash` são utilizados para organizar o estado interno das contas.
- **Polimorfismo:** a implementação dos métodos abstratos na classe derivada permite definir comportamentos específicos para as operações de exibição.

### Validação e regras de negócio

As operações possuem verificações para restringir valores inválidos, impedir saques acima do limite individual configurado e exigir autenticação em operações sensíveis, como saques e alterações cadastrais.

As movimentações são registradas em uma lista de extrato associada à conta.

### Autenticação

As senhas são transformadas em hashes SHA-256 para comparação durante a autenticação, evitando o armazenamento direto da senha em texto puro.

## Regras operacionais

| Operação | Regra implementada |
|---|---|
| Depósito | Valor mínimo de R$ 1,00 |
| Saque | Valor entre R$ 1,00 e R$ 500,00 por operação |
| Limite de saque | R$ 1.000,00 por instância de conta |
| Autenticação | Senha de seis caracteres no cadastro e validação nas operações protegidas |
| Alteração de titular | Exige senha e nome com pelo menos cinco caracteres |

## Como executar

### 1. Pré-requisitos

- Python 3 instalado.
- `pip` disponível para instalar a dependência externa.

### 2. Instale a dependência

```bash
pip install pwinput
```

### 3. Execute o sistema

Na pasta raiz do projeto, execute:

```bash
python main.py
```

O menu inicial permite criar uma conta, acessar uma conta existente ou encerrar o programa.

## Limitações conhecidas

- **Persistência:** as contas são armazenadas em um dicionário em memória. Os dados são perdidos quando o programa é encerrado.
- **Escopo:** o sistema não implementa banco de dados, API, autorização baseada em sessões persistentes ou integração com serviços financeiros reais.
- **Limite de saque:** o controle é mantido na instância da conta e não possui reinicialização automática diária.

## Objetivo do projeto

Consolidar os fundamentos de Python e Programação Orientada a Objetos por meio de uma aplicação prática, com separação de responsabilidades, implementação de regras de negócio e validação de operações.

O projeto também serve como base para evoluções futuras, como persistência em banco de dados, testes automatizados e exposição das funcionalidades por meio de uma API REST.