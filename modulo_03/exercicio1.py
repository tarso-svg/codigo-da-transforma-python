# Programa simples para exibir nome e tipo de dado

# Entrada do nome do usuário
nome = input("Digite seu nome: ")

# Exibindo mensagem personalizada
print("Olá,", nome + "! Seja muito bem-vindo ao mundo da programação em Python!")

# Exibindo o tipo da variável 'nome'
print("Tipo de dado da variável 'nome':", type(nome))

# Criar e gravar no arquivo
with open("dados.txt", "w") as arquivo:
    arquivo.write("Nome: Tarcísio\nIdade: 18\nCurso: Programação")

# Ler o arquivo
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo .txt:")
    print(conteudo)
import json

clientes = {
    "cliente1": {"nome": "Ana", "idade": 25},
    "cliente2": {"nome": "Carlos", "idade": 30}
}

# Salvar em JSON
with open("clientes.json", "w") as arquivo:
    json.dump(clientes, arquivo, indent=4)

# Ler do JSON
with open("clientes.json", "r") as arquivo:
    dados = json.load(arquivo)
    print("Clientes carregados do JSON:")
    print(dados)
import csv

# Adicionar notas
with open("notas.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Nota"])
    escritor.writerow(["Maria", 8.5])
    escritor.writerow(["João", 6.7])
    escritor.writerow(["Pedro", 9.2])

# Ler notas
with open("notas.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    print("Notas carregadas do CSV:")
    for linha in leitor:
        print(linha)
import shutil
import os

# Criar pastas exemplo
os.makedirs("origem", exist_ok=True)
os.makedirs("backup", exist_ok=True)

# Criar um arquivo de teste
with open("origem/arquivo.txt", "w") as f:
    f.write("Arquivo importante para backup!")

# Copiar todos os arquivos da pasta origem para backup
for arquivo in os.listdir("origem"):
    caminho_origem = os.path.join("origem", arquivo)
    caminho_destino = os.path.join("backup", arquivo)
    shutil.copy(caminho_origem, caminho_destino)

print("Backup concluído com sucesso!")
