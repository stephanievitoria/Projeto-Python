# 🏦 Mack Bank - Sistema Bancário em Python

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Status](https://img.shields.io/badge/Status-Finalizado-brightgreen?style=for-the-badge)

Este projeto é uma aplicação de **Sistema Bancário** desenvolvida como parte da disciplina de **Algoritmos e Programação** na **UPM (Universidade Presbiteriana Mackenzie)**. O objetivo foi aplicar conceitos fundamentais de lógica de programação, manipulação de variáveis, estruturas de repetição e funções em Python.

---

## Descrição do Projeto

O **Mack Bank** simula as operações essenciais de uma conta corrente, permitindo o gerenciamento de saldo, limite de crédito e segurança por senha. O projeto foca na validação rigorosa de dados e na experiência do usuário via terminal.

### Funcionalidades Principais

* **Cadastro de Conta:** * Geração automática de número de conta (ID aleatório).
    * Validação de CPF (11 dígitos numéricos).
    * Exigência de saldo inicial mínimo de **R$ 1.000,00**.
    * Criação de senha numérica de exatos 6 dígitos.
* **Depósito:** Incremento de saldo com verificação de segurança da conta.
* **Saque Inteligente:** * Verificação de saldo disponível somado ao limite de crédito.
    * Sistema de segurança: Bloqueio de operação após 3 tentativas de senha incorreta.
* **Consulta de Saldo & Extrato:** * Exibição do saldo e limite atualizados.
    * Histórico detalhado de todas as operações realizadas na sessão.

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Bibliotecas:** `random` (para geração de número da conta)
* **Conceitos Aplicados:**
    * Manipulação de variáveis globais e locais.
    * Estruturas de controle de fluxo (`if`, `elif`, `else`).
    * Laços de repetição para validação (`while`, `for`).
    * Tratamento de listas para histórico de operações.

---

## Como Executar

1.  Certifique-se de ter o **Python 3** instalado.
2.  Faça o download do arquivo do código (ex: `projeto_banco.py`).
3.  Abra o terminal ou prompt de comando na pasta do arquivo.
4.  Execute o programa:
    ```bash
    python projeto_banco.py
    ```

---

## Autoras

Projeto desenvolvido por alunos do 1º semestre do curso de **Sistemas de Informação**:

* **Joyce Cristina Pires Lima da Silva**
* **Stephanie Vitoria Soares da Cruz**

**Orientador:** Prof. André Rodrigues Oliveira

---

## Contexto Acadêmico

Este software foi o projeto prático consolidado para a matéria de Algoritmos na **UPM**, visando demonstrar a capacidade de estruturação de sistemas lógicos e resolução de problemas através de código limpo e funcional.
