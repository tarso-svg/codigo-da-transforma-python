# Programa simples para exibir nome e tipo de dado

# Entrada do nome do usuário
nome = input("Digite seu nome: ")

# Exibindo mensagem personalizada
print("Olá,", nome + "! Seja muito bem-vindo ao mundo da programação em Python!")

# Exibindo o tipo da variável 'nome'
print("Tipo de dado da variável 'nome':", type(nome))

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


# Teste
carro1 = Carro("Toyota", "Corolla")
carro1.exibir_info()
class CarroEletrico(Carro):  # herda de Carro
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        super().exibir_info()
        print(f"Autonomia da Bateria: {self.autonomia_bateria} km")


# Teste
carro2 = CarroEletrico("Tesla", "Model 3", 450)
carro2.exibir_info()
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo}"


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.autonomia_bateria} km de autonomia"


# Teste
carro1 = Carro("Fiat", "Uno")
carro2 = CarroEletrico("BYD", "Han", 520)

print(carro1)  
print(carro2)
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo}"


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.autonomia_bateria} km de autonomia"


# Teste
carro1 = Carro("Fiat", "Uno")
carro2 = CarroEletrico("BYD", "Han", 520)

print(carro1)  
print(carro2)

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} - {self.autor} ({status})"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def mostrar_livros(self):
        for livro in self.livros:
            print(livro)

    def emprestar(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                print(f"Você pegou emprestado: {livro.titulo}")
                return
        print("Livro não disponível.")

    def devolver(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and not livro.disponivel:
                livro.disponivel = True
                print(f"Você devolveu: {livro.titulo}")
                return
        print("Esse livro não está registrado como emprestado.")


# Teste
biblio = Biblioteca()
livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Dom Casmurro", "Machado de Assis")

biblio.adicionar_livro(livro1)
biblio.adicionar_livro(livro2)

biblio.mostrar_livros()
biblio.emprestar("1984")
biblio.mostrar_livros()
biblio.devolver("1984")
biblio.mostrar_livros()
