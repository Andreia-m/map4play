README.md 

## Requisitos 

Python 3.12.2 - Conferir a versão: python --version 

Django 5.2 - Conferir a versão: django-admin –version 

Git – Conferir a instalação: git -v 

 

## Sequência para criar o projeto 

Criar o ambiente virtual  

python –m venv venv 

 

Ativar o ambiente virtual 

venv\Scripts\activate 

 

Instalar o Django 

pip install django 

 

Criar o projeto com Django 

django-admin startproject sitequadras .  

 

Gerar o arquivo com as dependências 

Após instalar as dependências, execute o comando abaixo: 

pip freeze > requirements.txt 

 

Executar as migrations 

python manage.py migrate 

 

Rodar o projeto 

python manage.py runserver 

 

Acessar o padrão do Python 

http://127.0.0.1:8000/ 

 

Criar um super usuário 

python manage.py createsuperuser 

 

Acessar o sistema administrativo do python  

http://127.0.0.1:8000/admin/ 

 

Criar app 

python manage.py startapp quadras
