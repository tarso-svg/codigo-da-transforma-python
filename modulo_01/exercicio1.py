# Programa simples para exibir nome e tipo de dado

# Entrada do nome do usuário
nome = input("Digite seu nome: ")

# Exibindo mensagem personalizada
print("Olá,", nome + "! Seja muito bem-vindo ao mundo da programação em Python!")

# Exibindo o tipo da variável 'nome'
print("Tipo de dado da variável 'nome':", type(nome))

lista_compras = []

while True:
    print("\n1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar lista")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item para adicionar: ")
        lista_compras.append(item)
        print(f"{item} adicionado!")
    elif opcao == "2":
        item = input("Digite o item para remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"{item} removido!")
        else:
            print("Item não encontrado na lista.")
    elif opcao == "3":
        print("Lista de compras:", lista_compras)
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")
aluno = {
    "nome": "Maria",
    "idade": 16,
    "notas": [8.5, 9.0, 7.5]
}

print("Dados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Números pares:", pares)
print("Números ímpares:", impares)
agenda = {}

while True:
    print("\n1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Mostrar todos")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone
        print(f"Contato {nome} adicionado!")
    elif opcao == "2":
        nome = input("Nome do contato a remover: ")
        if nome in agenda:
            del agenda[nome]
            print(f"Contato {nome} removido!")
        else:
            print("Contato não encontrado.")
    elif opcao == "3":
        nome = input("Nome do contato: ")
        if nome in agenda:
            print(f"{nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")
    elif opcao == "4":
        print("Agenda de contatos:")
        for nome, tel in agenda.items():
            print(f"{nome}: {tel}")
    elif opcao == "5":
        break
    else:
        print("Opção inválida!")

