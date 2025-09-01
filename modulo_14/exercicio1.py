# Programa simples para exibir nome e tipo de dado

# Entrada do nome do usuário
nome = input("Digite seu nome: ")

# Exibindo mensagem personalizada
print("Olá,", nome + "! Seja muito bem-vindo ao mundo da programação em Python!")

# Exibindo o tipo da variável 'nome'
print("Tipo de dado da variável 'nome':", type(nome))

from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome
from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('create/', views.produto_create, name='produto_create'),
    path('update/<int:pk>/', views.produto_update, name='produto_update'),
    path('delete/<int:pk>/', views.produto_delete, name='produto_delete'),]
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/list.html', {'produtos': produtos})

def produto_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/form.html', {'form': form})

def produto_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/form.html', {'form': form})

def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('produto_list')
    return render(request, 'produtos/delete.html', {'produto': produto})
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade']
<h1>Lista de Produtos</h1>
<a href="{% url 'produto_create' %}">Novo Produto</a>
<ul>
  {% for produto in produtos %}
    <li>
      {{ produto.nome }} - R$ {{ produto.preco }} ({{ produto.quantidade }})
      <a href="{% url 'produto_update' produto.pk %}">Editar</a>
      <a href="{% url 'produto_delete' produto.pk %}">Excluir</a>
    </li>
  {% empty %}
    <li>Nenhum produto cadastrado</li>
  {% endfor %}
</ul>
<h1>Produto</h1>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Salvar</button>
</form>
<a href="{% url 'produto_list' %}">Voltar</a>
<h1>Excluir Produto</h1>
<p>Tem certeza que deseja excluir {{ produto.nome }}?</p>
<form method="post">
  {% csrf_token %}
  <button type="submit">Confirmar</button>
</form>
<a href="{% url 'produto_list' %}">Cancelar</a>
from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade')
    search_fields = ('nome',)
from django.test import TestCase
from .models import Produto

class ProdutoTest(TestCase):
    def setUp(self):
        Produto.objects.create(nome="Camiseta", descricao="Algodão", preco=50, quantidade=10)

    def test_criacao_produto(self):
        produto = Produto.objects.get(nome="Camiseta")
        self.assertEqual(produto.preco, 50)
from django.core.paginator import Paginator

def produto_list(request):
    search = request.GET.get('search')
    produtos = Produto.objects.all()
    if search:
        produtos = produtos.filter(nome__icontains=search)

    paginator = Paginator(produtos, 5)  # 5 produtos por página
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'produtos/list.html', {'produtos': produtos})
<form method="get">
  <input type="text" name="search" placeholder="Buscar produto..." value="{{ request.GET.search }}">
  <button type="submit">Buscar</button>
</form>

<ul>
  {% for produto in produtos %}
    <li>{{ produto.nome }} - R$ {{ produto.preco }}</li>
  {% endfor %}
</ul>

<div>
  {% if produtos.has_previous %}
    <a href="?page={{ produtos.previous_page_number }}&search={{ request.GET.search }}">Anterior</a>
  {% endif %}
  
  Página {{ produtos.number }} de {{ produtos.paginator.num_pages }}
  
  {% if produtos.has_next %}
    <a href="?page={{ produtos.next_page_number }}&search={{ request.GET.search }}">Próxima</a>
  {% endif %}
</div>