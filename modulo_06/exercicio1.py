# Programa simples para exibir nome e tipo de dado

# Entrada do nome do usuário
nome = input("Digite seu nome: ")

# Exibindo mensagem personalizada
print("Olá,", nome + "! Seja muito bem-vindo ao mundo da programação em Python!")

# Exibindo o tipo da variável 'nome'
print("Tipo de dado da variável 'nome':", type(nome))

def calculadora():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            print("Resultado:", a + b)
        elif operacao == "-":
            print("Resultado:", a - b)
        elif operacao == "*":
            print("Resultado:", a * b)
        elif operacao == "/":
            try:
                print("Resultado:", a / b)
            except ZeroDivisionError:
                print("Erro: divisão por zero não é permitida!")
        else:
            print("Operação inválida.")

    except ValueError:
        print("Erro: você precisa digitar números válidos.")

# Teste
# calculadora()
class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem="Saldo insuficiente para realizar o saque."):
        super().__init__(mensagem)

class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError
        self.saldo -= valor
        print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")

# Teste
conta = ContaBancaria(100)
conta.depositar(50)

try:
    conta.sacar(200)
except SaldoInsuficienteError as e:
    print(e)
def cadastrar_usuario():
    nome = input("Digite seu nome: ")

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade <= 0:
                raise ValueError("A idade deve ser um número positivo.")
            break
        except ValueError as e:
            print("Erro:", e)

    print(f"Usuário cadastrado: {nome}, {idade} anos")

# Teste

# cadastrar_usuario()
def sistema_login():
    usuario_correto = "admin"
    senha_correta = "1234"
    tentativas = 3

    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("Login bem-sucedido! 🎉")
            return
        else:
            tentativas -= 1
            print(f"Credenciais inválidas. Tentativas restantes: {tentativas}")

    print("Acesso bloqueado! Muitas tentativas falhas.")

# Teste
# sistema_login()