#Sistema de conta corrente bancária
import random

conta_cadastrada = None
saldo = 0
numero_da_conta = random.randint(1000, 9999)
nome_do_cliente = None
historico_de_operações = []
saldo_inicial = 0
limite_credito = 0
deposito = 0
senha = None
    
    #PRIMEIRA OPÇÃO - CADASTRAR CONTA
def cadastrar_conta():
    global conta_cadastrada, nome_do_cliente, numero_da_conta, saldo, limite_credito, senha

    if conta_cadastrada:
        print("ESSA CONTA JÁ ESTÁ EM USO! RETORNE AO MENU PRINCIPAL")
        return

    print("MACK BANK – CADASTRO DE CONTA")
    
    #Número aleatório da conta
    print(f"NÚMERO DA CONTA: {numero_da_conta}")

    #Obter informações do usuário
    nome_do_cliente = input("NOME DO CLIENTE: ").strip()
    if not nome_do_cliente:
        print("ERRO! INSIRA O SEU NOME")
        return
    #ADICIONAL DO NOSSO PROJETO
    cpf = input("INFORME O CPF: ")
    while cpf.isdecimal() and len(cpf) == 11:
        break
    else:
        print("ERRO: O CPF não está completo ou correto")
        return
    telefone = input("TELEFONE.......: ").strip()
    if not telefone:
        print("ERRO! INSIRA O SEU NUMERO DE TELEFONE")
        return 
    email = input("EMAIL..........: ").strip()
    if not email:
        print("ERRO! INSIRA O SEU EMAIL")
        return 

    #Validando entrada de saldo inicial
    saldo = float(input("SALDO INICIAL...: R$ "))
    if saldo < 1000:
        print("O SALDO DEVE SER MAIOR QUE 1000")
        return

    #Validando entrada do limite de crédito
    limite_credito = float(input("LIMITE DE CRÉDITO: R$ "))
    while limite_credito < 0:
        print("O LIMITE DEVE SER IGUAL OU MAIOR QUE 0")

    #Validando entrada da senha
    senha = input("SENHA............: ")
    repetir_senha = input("REPITA A SENHA...: ")
    while senha == repetir_senha and senha.isdecimal() and len(senha) == 6:
        break
    else:
        print("ERRO: As senhas contém letras, não coincidem ou não tem 6 caracteres")
        #SEGUNDO ADICIONAL: a senha só pode conter números
        return

    print("CADASTRO REALIZADO!")

    #SEGUNDA OPÇÃO - DEPOSITAR

def depositar():
    global historico_de_operações, saldo, numero_da_conta, nome_do_cliente

    print('MACK BANK - DEPÓSITO NA CONTA')

    #Inserindo conta cadastrada
    conta_digitada = input('INFORME O NÚMERO DA CONTA: ')

    #Verificar se a conta coincide
    if conta_digitada == str(numero_da_conta):
        print('NOME DO CLIENTE:', nome_do_cliente)
    else:
        print("NUMERO DA CONTA INVALIDO. RETORNANDO AO MENU PRINCIPAL.")
        return 

    #Solicitando valor do depósito
    while True:
        deposito = float(input("VALOR DO DEPÓSITO: R$ "))
        if deposito > 0:
            break
        else:
            print("ERRO: VALOR INVÁLIDO! DIGITE NOVAMENTE")

    #Registrar a operação no histórico
    historico_de_operações.append(f"Depósito feito no valor de R${deposito}")
    saldo += deposito

    print("DEPÓSITO REALIZADO COM SUCESSO! Saldo atual: R$", saldo)
    return saldo


    #TERCEIRA OPÇÃO - SACAR
def sacar():
    global saldo, historico_de_operações, limite_credito, senha
    print("MACK BANK – SAQUE DA CONTA")

    #Inserindo conta cadastrada
    conta_digitada = input('INFORME O NÚMERO DA CONTA: ')

    #Verificar se a conta coincide
    if conta_digitada == str(numero_da_conta):
        print('NOME DO CLIENTE:', nome_do_cliente)
    else:
        print("NUMERO DA CONTA INVALIDO. RETORNANDO AO MENU PRINCIPAL")
        return
    #Inserir senha cadastrada
    senha_digitada = input("INFORME A SENHA: ")

    #Verificar se senha coincide
    contadora = 0 
    while senha_digitada != senha and contadora < 2:
        print("SENHA INCORRETA")
        
        senha_digitada = input("INFORME A SENHA: ")
        contadora += 1
    if senha_digitada != senha:
        print ("CONTA BLOQUEADA! NÚMERO DE TENTATIVAS EXCEDIDO")
        tentativas_bloqueio += 1
        return

     #Inserir valor de saque
    valor_saque = float(input("VALOR DO SAQUE: R$ "))

    if saldo >= valor_saque:
        saldo -= valor_saque
        historico_de_operações.append(f"SAQUE: -R$ {valor_saque}")
        print("SAQUE REALIZADO COM SUCESSO! SALDO ATUAL: R$", saldo)
    elif saldo + limite_credito >= valor_saque:
        saldo -= valor_saque
        limite_credito -= valor_saque
        historico_de_operações.append(f"SAQUE (LIMITE DE CRÉDITO): -R$ {valor_saque}")
        print("VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO")
    else:
        print("SALDO INSUFICIENTE E LIMITE DE CRÉDITO EXCEDIDO")


    #QUARTA OPÇÃO - CONSULTAR SALDO
def consultar_saldo():
    global saldo, limite_credito
    print("MACK BANK – CONSULTA SALDO")
    #Inserindo conta cadastrada
    conta_digitada = input('INFORME O NÚMERO DA CONTA: ')

    #Verificar se a conta coincide
    if conta_digitada == str(numero_da_conta):
        print('NOME DO CLIENTE:', nome_do_cliente)
    else:
        print("NUMERO DA CONTA INVALIDO. RETORNANDO AO MENU PRINCIPAL.")
        return
    #Inserir senha cadastrada
    senha_digitada = input("INFORME A SENHA: ")

    #Verificar se senha coincide
    contadora = 0 
    while senha_digitada != senha and contadora < 2:
        print("SENHA INCORRETA")
        
        senha_digitada = input("INFORME A SENHA: ")
        contadora += 1
    if senha_digitada != senha:
        print ("CONTA BLOQUEADA! NÚMERO DE TENTATIVAS EXCEDIDO")
        tentativas_bloqueio += 1
        return
 

  
    print(f"SALDO EM CONTA: R$ {saldo}")
    print(f"LIMITE DE CRÉDITO: R$ {limite_credito}")
    input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
    return

    #QUINTA OPÇÃO - CONSULTAR EXTRATO
def consultar_extrato():
    global historico_de_operações, limite_credito, saldo, senha
    print("MACK BANK – CONSULTAR EXTRATO")
    
   #Inserindo conta cadastrada
    conta_digitada = input('INFORME O NÚMERO DA CONTA: ')

    #Verificar se a conta coincide
    if conta_digitada == str(numero_da_conta):
        print('NOME DO CLIENTE:', nome_do_cliente)
    else:
        print("NUMERO DA CONTA INVALIDO. RETORNANDO AO MENU PRINCIPAL.")
        return
    #Inserir senha cadastrada
    senha_digitada = input("INFORME A SENHA: ")

    #Verificar se senha coincide
    contadora = 0 
    while senha_digitada != senha and contadora < 2:
        print("SENHA INCORRETA")
        
        senha_digitada = input("INFORME A SENHA: ")
        contadora += 1
    if senha_digitada != senha:
        print ("CONTA BLOQUEADA! NÚMERO DE TENTATIVAS EXCEDIDO")
        tentativas_bloqueio += 1
        return
 

    print(f"LIMITE DE CRÉDITO: R$ {limite_credito}")
    print("ÚLTIMAS OPERAÇÕES:")
    for operacao in historico_de_operações:
        print(operacao)
    print(f"SALDO EM CONTA: R$ {saldo}")
    if saldo < 0:
        print("Atenção ao seu saldo!")
    
    #Loop principal do programa
while True:
    print("MACK BANK – ESCOLHA UMA OPÇÃO")
    print("(1) CADASTRAR CONTA CORRENTE")
    print("(2) DEPOSITAR")
    print("(3) SACAR")
    print("(4) CONSULTAR SALDO")
    print("(5) CONSULTAR EXTRATO")
    print("(6) FINALIZAR")

    opcao = input("SUA OPÇÃO: ")

    if opcao == '1':
        cadastrar_conta()
    elif opcao == '2':
         depositar()
    elif opcao == '3':
        sacar()
    elif opcao == '4':
        consultar_saldo()
    elif opcao == '5':
        consultar_extrato()
    elif opcao == '6':
        print("MACK BANK – SOBRE")
        print("Este programa foi desenvolvido por")
        print ("Joyce Cristina Pires Lima da Silva")
        print ("Stephanie Vitoria Soares da Cruz")
        break
    else:
        print("Opção Inválida! Digite um número entre 1 e 6")


   

