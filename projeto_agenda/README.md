# Projeto Agenda - Django

Projeto de agenda feito com Django e SQLite.

## Configuração do ambiente

Neste projeto estou utilizando UV como gerenciador de pacotes. Para mais informações, acesse a documentação oficial [aqui](https://docs.astral.sh/uv/getting-started/installation/).

### Comandos

```
uv init
uv venv
uv add django
django-admin startproject project .
python manage.py startapp contact
python manage.py runserver
```

Após criar o app, é necessário referenciar o app no arquivo settings.py, no argumento INSTALLED_APPS.

```
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
