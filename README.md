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

Caso seja criado uma pasta de templates (ex: base) com arquivos globais (ex: partials e layouts que serão usados em várias páginas ou projetos diferentes), é preciso adicionar o módulo ao settings.py no módulo TEMPLATES, na chave DIRS. O módulo STATICFILES_DIRS é usado para arquivos estáticos (css, js, imagens).

## Django HTML

O comando abaixo herda o template base.html para o template atual.
`{% extends "base.html" %}`

O comando abaixo imprime o conteúdo dentro do bloco `texto`
`{% block texto %} {% endblock texto %}`

Caso algum dado seja passado da view (python) para o HTML, é preciso passar o contexto para a view como parâmetro chave-valor:
`return render(request, 'estudos_django/index.html', {'nome': 'João'})`. No HTML, é preciso inserir o comando `{{ nome }}` para imprimir o conteúdo da variável nome.