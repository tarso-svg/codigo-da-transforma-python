# Programa simples para exibir nome e tipo de dado

# Entrada do nome do usuário
nome = input("Digite seu nome: ")

# Exibindo mensagem personalizada
print("Olá,", nome + "! Seja muito bem-vindo ao mundo da programação em Python!")

# Exibindo o tipo da variável 'nome'
print("Tipo de dado da variável 'nome':", type(nome))

def calcular_media(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        print(f"Média {media:.2f} - Aluno aprovado!")
    else:
        print(f"Média {media:.2f} - Aluno reprovado!")

# Exemplo de uso
calcular_media([8, 6, 7])
def calcular_media(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        print(f"Média {media:.2f} - Aluno aprovado!")
    else:
        print(f"Média {media:.2f} - Aluno reprovado!")

# Exemplo de uso
calcular_media([8, 6, 7])
def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor

# Exemplo de uso
numeros = [3, 10, 1, 8, 5]
maior, menor = maior_menor(numeros)
print(f"Maior: {maior}, Menor: {menor}")
def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor

# Exemplo de uso
numeros = [3, 10, 1, 8, 5]
maior, menor = maior_menor(numeros)
print(f"Maior: {maior}, Menor: {menor}")

usuarios = {
    "admin": "1234",
    "tarcisio": "senha123"
}

def login(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return "Login bem-sucedido!"
    else:
        return "Usuário ou senha inválidos."

# Exemplo de uso
print(login("tarcisio", "senha123"))
print(login("admin", "9999"))
