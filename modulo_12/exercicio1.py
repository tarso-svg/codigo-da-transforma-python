# Programa simples para exibir nome e tipo de dado

# Entrada do nome do usuário
nome = input("Digite seu nome: ")

# Exibindo mensagem personalizada
print("Olá,", nome + "! Seja muito bem-vindo ao mundo da programação em Python!")

# Exibindo o tipo da variável 'nome'
print("Tipo de dado da variável 'nome':", type(nome))

def soma(a, b):
    return a + b
import unittest
from main import soma

class TestSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
class Calculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não permitida")
        return a / b
import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calc.somar(10, 5), 15)
        self.assertEqual(self.calc.somar(-1, 1), 0)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertAlmostEqual(self.calc.dividir(7, 3), 2.3333, places=4)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()
# app.py
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})
# test_app.py
from app import app

def test_ping():
    client = app.test_client()
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "pong"}