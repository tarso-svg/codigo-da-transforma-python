# Programa simples para exibir nome e tipo de dado

# Entrada do nome do usuário
nome = input("Digite seu nome: ")

# Exibindo mensagem personalizada
print("Olá,", nome + "! Seja muito bem-vindo ao mundo da programação em Python!")

# Exibindo o tipo da variável 'nome'
print("Tipo de dado da variável 'nome':", type(nome))

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# --- Criar banco e tabela ---
def init_db():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    conn.close()

# Inicializa o banco ao rodar o servidor
init_db()

# --- 1. Rota GET /saudacao ---
@app.route("/saudacao", methods=["GET"])
def saudacao():
    return jsonify({"mensagem": "Olá, bem-vindo à API com Flask!"})


# --- 2. Rota POST /cadastrar ---
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email
{
  "nome": "Maria",
  "email": "maria@email.com"}
