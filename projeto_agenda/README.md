# Projeto Agenda - Django

Projeto de agenda feito com Django e SQLite.

## Configuração do ambiente

Neste projeto estou utilizando UV como gerenciador de pacotes. Para mais informações, acesse a documentação oficial [aqui](https://docs.astral.sh/uv/getting-started/installation/).

### Comandos

```bash
uv init
uv venv
uv add django
django-admin startproject project .
python manage.py startapp contact
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Após criar o app, é necessário referenciar o app no arquivo settings.py, no argumento INSTALLED_APPS.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contact',
]
```

Criar as pastas de templates e arquivos estáticos globais (que podem ser reutilizados em vários apps).

```
├── base_static
│   └── global
│       └── css
│           └── style.css
└── base_templates
    └── global
        └── base.html
```

O arquivo base.html acima deve referenciar os arquivos estáticos globais com os comandos `{% load static %}` e `{% static 'global/css/style.css' %}`, conforme exemplo abaixo:

```django
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'global/css/style.css' %}">
</head>

<body>
    <h1>Base</h1>
</body>

</html>

```

Após criar as pastas globais acima, é preciso referenciar o argumento TEMPLATES e STATICFILES_DIRS no settings.py.

```python
TEMPLATES = [
    DIRS = [
        BASE_DIR / 'base_templates',
    ]
]

STATICFILES_DIRS = [
    BASE_DIR / 'base_static',
]
```

Criar a pasta de templates para o app.

```
└── contact
    └── templates
        └── contact
            └── index.html
```

O arquivo index.html acima herda o arquivo base.html da pasta global.

```django
{% extends 'global/base.html' %}
```

Criar o arquivo urls.py para o app e referenciar a URL no urls.py do projeto. No exemplo abaixo precisei criar uma função index no views.py do app.

```python
# contact/urls.py
from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]

# contact/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'contact/index.html')

# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contact.urls')),
]

