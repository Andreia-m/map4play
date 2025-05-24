README.md 

## Requisitos 

Python 3.12.2 - Conferir a versão: python --version 

Django 5.2 - Conferir a versão: django-admin –-version 

Git – Conferir a instalação: git -v 

 

## Como rodar o projeto baixado 

Baixar o projeto do GitHub:

    git clone https://github.com/Andreia-m/map4play.git .


Criar o ambiente virtual:  

    python –m venv venv 

 
Ativar o ambiente virtual: 

    venv\Scripts\activate 

 
Instalar as dependências: 

    pip install -r requirements.txt


Executar as migration para criar as tabelas no banco de dados: 

    python manage.py migrate 


Criar o super usuário: 

    python manage.py createsuperuser 
 

Rodar o projeto: 

    python manage.py runserver 

 
Acessar o padrão do Python: 

    http://127.0.0.1:8000/ 


Acessar o sistema administrativo padrão do Django:
    http://127.0.0.1:8000/admin

