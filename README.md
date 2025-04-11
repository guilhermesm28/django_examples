# Estudos Django

## Criar um projeto Django

Cria uma pasta com o nome estudos_django e os arquivos de configuração do Django:
`django-admin startproject estudos_django`

Cria uma pasta com o nome estudos_django e os arquivos de configuração do Django na pasta atual:
`django-admin startproject estudos_django .`

## Executar uma aplicação Django

Executa o servidor do Django:
`python manage.py runserver`

Criar um app Django:
`python manage.py startapp estudos_django`

## Configurações no settings.py

O settings.py contém as configurações do Django. As configurações são organizadas em módulos.

Para ver as configurações disponíveis, digite:
`python manage.py show_settings`

Se um novo app for criado, é preciso adicionar o módulo ao settings.py no módulo INSTALLED_APPS