# Programa simples para exibir nome e tipo de dado

# Entrada do nome do usuário
nome = input("Digite seu nome: ")

# Exibindo mensagem personalizada
print("Olá,", nome + "! Seja muito bem-vindo ao mundo da programação em Python!")

# Exibindo o tipo da variável 'nome'
print("Tipo de dado da variável 'nome':", type(nome))

import requests

API_KEY = "SUA_CHAVE_AQUI"
cidade = "São Paulo"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()  # Lança erro se status != 200
    dados = resposta.json()
    
    print("Dados brutos da API:")
    print(dados)

except requests.exceptions.RequestException as e:
    print("Erro ao acessar a API:", e)
import requests

API_KEY = "SUA_CHAVE_AQUI"
cidade = "São Paulo"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()

    temperatura = dados["main"]["temp"]
    sensacao = dados["main"]["feels_like"]
    clima = dados["weather"][0]["description"]

    print(f"🌡️ Temperatura atual: {temperatura}°C")
    print(f"🤔 Sensação térmica: {sensacao}°C")
    print(f"⛅ Condições: {clima}")

except requests.exceptions.RequestException as e:
    print("Erro na conexão:", e)
except KeyError:
    print("Erro ao processar os dados da API.")
import requests

API_KEY = "SUA_CHAVE_TMDB"
filme = "Inception"
url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={filme}&language=pt-BR"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()

    if dados["results"]:
        filme_info = dados["results"][0]
        print("🎬 Título:", filme_info["title"])
        print("📅 Data de lançamento:", filme_info["release_date"])
        print("⭐ Nota:", filme_info["vote_average"])
        print("📝 Sinopse:", filme_info["overview"])
    else:
        print("Nenhum filme encontrado.")

except requests.exceptions.RequestException as e:
    print("Erro ao acessar a API do TMDB:", e)
