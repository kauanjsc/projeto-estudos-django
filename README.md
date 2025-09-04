-  Projeto de Estudos Django

Este é um projeto simples desenvolvido com **Django** para fins de estudo.  
Aqui vou praticar conceitos como models, views, templates, autenticação e muito mais.

GP - Sistema de Gestão de Produtos

Esse é um mini projeto feito em Django para treinar e melhorar meus conhecimentos.
A ideia foi criar um sistema simples para gerenciar produtos, marcas e categorias, usando também o Jazzmin para deixar o painel do admin mais bonito.

Funcionalidades

Cadastro de produtos, marcas e categorias

Filtros e buscas no admin

Exportação de produtos para CSV

Painel administrativo customizado com Jazzmin

Tecnologias

Python 3.10+

Django 5.x

SQLite (banco de dados padrão)

Jazzmin (tema para Django Admin)

Como rodar o projeto

Clone o repositório:

git clone https://github.com/kauanjsc/sgp.git
cd sgp


Crie o ambiente virtual e ative:

python -m venv venv
venv\Scripts\activate


Instale as dependências:

pip install -r requirements.txt


Rode as migrações e crie o superusuário:

python manage.py migrate
python manage.py createsuperuser


Execute o servidor:

python manage.py runserver


Depois é só acessar http://localhost:8000/admin
 para usar o sistema.

 Estrutura básica
SGP/
├── core/        # Configurações principais
├── products/    # App de produtos, marcas e categorias
├── templates/   # Templates HTML
├── manage.py
└── requirements.txt