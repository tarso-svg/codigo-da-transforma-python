# Programa simples para exibir nome e tipo de dado

# Entrada do nome do usuário
nome = input("Digite seu nome: ")

# Exibindo mensagem personalizada
print("Olá,", nome + "! Seja muito bem-vindo ao mundo da programação em Python!")

# Exibindo o tipo da variável 'nome'
print("Tipo de dado da variável 'nome':", type(nome))

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def potencia(a, b):
    return a ** b
import utilidades

print("Soma:", utilidades.soma(5, 3))
print("Subtração:", utilidades.subtracao(10, 4))
print("Potência:", utilidades.potencia(2, 3))
from faker import Faker

fake = Faker("pt_BR")

for i in range(3):
    print("Nome:", fake.name())
    print("Endereço:", fake.address())
    print("Email:", fake.email())
    print("-" * 30)
from datetime import datetime, timedelta

agora = datetime.now()
print("Agora:", agora)

futuro = agora + timedelta(days=7)
print("Daqui 7 dias:", futuro)
import random
import math

numero_secreto = random.randint(1, 100)
tentativas = 0

print("🎲 Jogo de Adivinhação 🎲")
print("Tente adivinhar o número entre 1 e 100!")

while True:
    palpite = int(input("Seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    else:
        print("Muito alto! Tente novamente.")

# Cálculo extra com math
print("Dica: A raiz quadrada do número secreto é aproximadamente:",
      round(math.sqrt(numero_secreto), 2))
meu_projeto/
│── main.py
│── matematica/
│     └── operacoes.py
│── jogo/
│     └── adivinhacao.py
def soma(a, b):
    return a + b

def potencia(a, b):
    return a ** b
import random

def jogar():
    numero = random.randint(1, 10)
    palpite = int(input("Adivinhe um número entre 1 e 10: "))
    if palpite == numero:
        print("Acertou!")
    else:
        print(f"Errou! O número era {numero}").
from matematica import operacoes
from jogo import adivinhacao

print("Soma:", operacoes.soma(3, 7))
print("Potência:", operacoes.potencia(2, 4))

adivinhacao.jogar()
