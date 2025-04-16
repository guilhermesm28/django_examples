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

O argumento STATIC_ROOT serve para armazenar os arquivos estáticos gerados pelo Django no servidor (no momento do deploy). Após configurar no settings.py, é preciso executar o comando `python manage.py collectstatic`.

```python
STATIC_ROOT = BASE_DIR / 'static'
```

Caso o projeto tenha a necessidade de receber arquivos de upload, é preciso referenciar os argumentos MEDIA_URL e MEDIA_ROOT no settings.py.

```python
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Esses diretórios de media e static vão ser criados na raiz do projeto e devem ser ignorados no .gitignore.

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
```

No arquivo settings.py é possível alterar o timezone e idioma. Para isso, basta ajustar os argumentos TIME_ZONE e LANGUAGE_CODE.

```python
TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'
```

Caso o projeto tenha mais de um ambiente (desenvolvimento e produção), é possível criar um arquivo settings_local.py e referenciar ele no settings.py. Porém, esse arquivo de configuração **deve ser ignorado no .gitignore.**

```python
# settings.py
try:
    from project.settings_local import *
except ImportError:
    pass

# settings_local.py
SECRET_KEY = 'CHANGE-ME'
DEBUG = True
# outras configurações de desenvolvimento aqui
```

## Models

Sempre que um model for criado ou modificado, é preciso executar os comandos abaixo.

```bash
python manage.py makemigrations
python manage.py migrate
```

É interessante também registrar os models no admin.py do app para que eles sejam visíveis no admin e possibilitem a interação com o banco de dados (CRUD) por meio da interface do Django.

```python
from django.contrib import admin
from contact.models import Contact

admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'created_date')
    search_fields = ('id', 'first_name', 'last_name', 'phone', 'email')
    list_filter = ('created_date',)
    list_per_page = 10
    list_max_show_all = 100
```