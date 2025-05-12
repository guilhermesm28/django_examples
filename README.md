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

Para adicionar esses partials, basta usar o comando `{% include "base/partials/_header.html" %}`

## Django HTML

O comando abaixo herda o template base.html para o template atual.
`{% extends "base.html" %}`

O comando abaixo imprime o conteúdo dentro do bloco `texto`
`{% block texto %} {% endblock texto %}`

Caso algum dado seja passado da view (python) para o HTML, é preciso passar o contexto para a view como parâmetro chave-valor:
`return render(request, 'estudos_django/index.html', {'nome': 'João'})`. No HTML, é preciso inserir o comando `{{ nome }}` para imprimir o conteúdo da variável nome.

O comando abaixo passa URLs dinâmicas para o template.
`{% url 'estudos_django' %}`. No arquivo urls.py, é preciso passar o argumento name='estudos_django' para a URL. Também é uma boa prática criar um namespace para as URLs. Dessa forma, se houver duas páginas home para URLs diferentes, eles serão chamados de estudos_django_2:home e estudos_django:home. Para isso, basta criar uma variável app_name no arquivo urls.py com o nome desejado para o namespace.

Para fazer um for no HTML: `{% for item in items %} {{ item }} {% endfor %}`. No arquivo views.py, é preciso passar o argumento items para a view. O mesmo é possível para while `{% while %} {% endwhile %}` e if `{% if %} {%  endif %}`.

## Deploy Django

No arquivo settings.py, é preciso passar o argumento STATIC_ROOT para a pasta onde os arquivos estarão. O próximo passo é instalar o whitenoise e configurar o middleware para servir os arquivos estáticos.
O comando abaixo gera os arquivos estáticos (css, js, imagens). É necessário executar esse comando antes de subir o projeto para o servidor.
`python manage.py collectstatic`.

Também no arquivo settings.py, é preciso mudar o argumento DEBUG para False e definir os hosts permitidos no argumento ALLOWED_HOSTS.

Comando para gerar o SECRET_KEY: `python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"`
