# Programa simples para exibir nome e tipo de dado

# Entrada do nome do usuário
nome = input("Digite seu nome: ")

# Exibindo mensagem personalizada
print("Olá,", nome + "! Seja muito bem-vindo ao mundo da programação em Python!")

# Exibindo o tipo da variável 'nome'
print("Tipo de dado da variável 'nome':", type(nome))

import sqlite3

# Conectar ao banco (vai criar se não existir)
conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")

conexao.commit()
conexao.close()
print("Tabela criada com sucesso!")
import sqlite3

def inserir_cliente(nome, email):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()
    print("Cliente inserido com sucesso!")

def listar_clientes():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    for linha in cursor.fetchall():
        print(linha)
    conexao.close()

def atualizar_cliente(id, novo_nome, novo_email):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?", (novo_nome, novo_email, id))
    conexao.commit()
    conexao.close()
    print("Cliente atualizado com sucesso!")

def deletar_cliente(id):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
    conexao.commit()
    conexao.close()
    print("Cliente deletado com sucesso!")
def clientes_com_a():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nome LIKE 'A%'")
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)
    conexao.close()
def menu():
    while True:
        print("\n=== Sistema de Clientes ===")
        print("1 - Inserir cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Deletar cliente")
        print("5 - Listar clientes com nome começando com 'A'")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            inserir_cliente(nome, email)
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            id = int(input("ID do cliente: "))
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            atualizar_cliente(id, nome, email)
        elif opcao == "4":
            id = int(input("ID do cliente: "))
            deletar_cliente(id)
        elif opcao == "5":
            clientes_com_a()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

# Executar menu
# menu()
