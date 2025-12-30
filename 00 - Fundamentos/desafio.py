menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Usuário
[l] Listar Usuários
[a] Criar Conta Corrente
[b] Listar Contas Correntes
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = {}
contas = {}

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1
    
    return saldo, extrato

def criar_usuario(cpf, nome, data_nasc, logradouro, nro, bairro, cidade, estado):
    global usuarios

    cpf = cpf.replace(",", "").replace("-", "")

    if cpf in usuarios:
        return False
    else: 
        usuarios = { 
                    cpf: { 
                        "nome": nome, 
                        "data_nasc": data_nasc, 
                        "endereco": {
                            "logradouro": logradouro, 
                            "nro": nro, 
                            "bairro": bairro, 
                            "cidade": cidade, 
                            "estado": estado
                        }
                    }
        } 
        return True

'''
def visualizar_historico():
'''
def criar_conta_corrente(cpf):
    global contas, usuarios
    
    if usuarios.get(cpf):
        contas = {
                    cpf: { 
                        "agencia":"0001", 
                        "conta_corrente": str(len(contas)+1)
                    }
        }
        return True
    else:
        return False

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "c":
        print("Por favor, informe os dados do cliente: \n")
        nome = input("Nome: ")
        data_nasc = input("Data de Nascimento: ")
        cpf = input("CPF:")
        logradouro = input("Logradouro: ")
        nro = input("Número: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")

        if criar_usuario(cpf=cpf, nome=nome, data_nasc=data_nasc, logradouro=logradouro, nro=nro, bairro=bairro, cidade=cidade, estado=estado):
            print("\nUsuário criado com sucesso!")
        else:
            print("\nErro ao criar usuário! Já existe um usuário com esse CPF!") 
    
    elif opcao == "l":
        print("\nUsuários Cadastrados:\n")
        print(usuarios)
        print("==========================================\n")

    elif opcao == "a":
        print("Por favor, informe os dados do cliente: \n")
        cpf = input("CPF:")
        if criar_conta_corrente(cpf):
            print("\nConta corrente criada com sucesso!")
        else:
            print("\nConta corrente não pôde ser criada, verifique se o cliente com o CPF informado está cadastrado.")

    elif opcao == "b":
        print("\nContas Correntes Cadastradas:\n")
        for chave, valor in contas.items():
            print("AG: " + valor["agencia"] + " / Conta Corrente: " + valor["conta_corrente"] + " => Cliente: " + usuarios[chave]["nome"] + "\n")
        
        print("==========================================\n")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
