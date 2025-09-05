# SGP - Sistema de Gestão de Produtos

Este é um projeto simples desenvolvido com **Django** para fins de estudo.  
O objetivo é praticar conceitos como models, views, templates, autenticação e muito mais.

## Sobre o Projeto

Este mini projeto foi criado para treinar e aprimorar conhecimentos em Django.  
A ideia é gerenciar produtos, marcas e categorias, utilizando também o Jazzmin para personalizar o painel administrativo.

## Funcionalidades

- Cadastro de produtos, marcas e categorias
- Filtros e buscas no admin
- Exportação de produtos para CSV
- Painel administrativo customizado com Jazzmin

## Tecnologias Utilizadas

- Python 3.10+
- Django 5.x
- SQLite (banco de dados padrão)
- Jazzmin (tema para Django Admin)

## Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/kauanjsc/sgp.git
   cd sgp
   ```

2. **Crie o ambiente virtual e ative:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Rode as migrações e crie o superusuário:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Execute o servidor:**
   ```bash
   python manage.py runserver
   ```

6. **Acesse o sistema:**
   - Abra [http://localhost:8000/admin](http://localhost:8000/admin) no navegador para usar o painel administrativo.

## Estrutura Básica do Projeto

```
SGP/
├── core/        # Configurações principais
├── products/    # App de produtos, marcas e categorias
├── templates/   # Templates HTML
├── manage.py
└── requirements.txt
```
