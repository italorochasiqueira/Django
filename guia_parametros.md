# 📘 Guia Completo de Django

## 1. Criar e ativar um ambiente virtual

```bash
python -m venv venv
```

Ativar:

- **Windows:**  
  `venv\Scripts\activate`

- **Linux/Mac:**  
  `source venv/bin/activate`

---

## 2. Instalar o Django

```bash
pip install django
```

---

## 3. Criar um projeto Django

```bash
django-admin startproject project .
```

> O ponto no final (`.`) indica que o projeto será criado dentro da pasta atual.

### Executar o servidor:

```bash
python manage.py runserver
```

---

## 4. Criar um App

```bash
python manage.py startapp home
```

> O App representa um módulo funcional do sistema.

---

## 5. Registrar o App no projeto

No arquivo `project/settings.py`, adicione:

```python
INSTALLED_APPS = [
    ...,
    'home',
]
```

---

## 6. Criar Views

`home/views.py`:

```python
from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")
```

---

## 7. Criar e aninhar URLs do App

Crie `home/urls.py`:

```python
from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]
```

Aninhe no arquivo `project/urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
]
```

---

## 8. Criar Templates

Estrutura:

```
home/
 └─ templates/
      └─ home.html
```

Uso em views:

```python
return render(request, "home.html")
```

---

## 9. Registrar Templates Globais

Criar pasta:

```
project/
 └─ templates/
      └─ base.html
```

Adicionar ao `settings.py`:

```python
'DIRS': [BASE_DIR / "templates"],
```

---

## 10. Arquivos Estáticos (CSS, JS, imagens)

Estrutura:

```
home/
 └─ static/
      ├─ css/
      ├─ js/
      └─ img/
```

Configuração no `settings.py`:

```python
STATIC_URL = 'static/'
```

Uso nos templates:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

Para produção:

```bash
python manage.py collectstatic
```

---

## 11. Templates Base (Herança)

`templates/base.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Sistema Django</title>
</head>
<body>
    {% block conteudo %}{% endblock %}
</body>
</html>
```

`home.html`:

```html
{% extends "base.html" %}
{% block conteudo %}
<h1>Página Inicial</h1>
{% endblock %}
```

---

## 12. Banco de Dados e Models

`home/models.py`:

```python
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
```

Criar tabelas:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 13. Django Admin

Criar superusuário:

```bash
python manage.py createsuperuser
```

Registrar modelo:

`home/admin.py`:

```python
from django.contrib import admin
from .models import Pessoa

admin.site.register(Pessoa)
```

---

# 📂 Estrutura de Pastas Recomendada

```
project/
│   manage.py
│
├── project/
│     ├── settings.py
│     ├── urls.py
│     ├── wsgi.py
│     └── asgi.py
│
├── templates/
│     └── base.html
│
├── static/
│     ├── css/
│     ├── js/
│     └── img/
│
└── home/
      ├── migrations/
      ├── templates/
      │     └── home.html
      ├── static/
      │     └── home/
      ├── models.py
      ├── views.py
      ├── urls.py
      └── admin.py
```

---

Arquivo gerado automaticamente.
