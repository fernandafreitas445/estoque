# EstoquePro - Sistema de Gerenciamento de Estoque

Este é um projeto completo desenvolvido em Django e Django REST Framework para gerenciamento de estoque de loja.

## Funcionalidades
- **Interface Web**: Desenvolvida com HTML, CSS e Bootstrap.
- **CRUD**: Cadastro, listagem, edição e exclusão de Produtos, Categorias e Movimentações com controle de quantidade.
- **Autenticação e Autorização**: Listagem de produtos é pública. As operações de manipulação (CRUD) restritas para usuários com login.

## Como Executar Localmente

1. Crie um ambiente virtual: python -m venv venv

2. Instale as dependências: pip install django djangorestframework django-cors-headers

3. Aplique as migrações: python manage.py migrate

4. Crie um superusuário: python manage.py createsuperuser

5. Inicie o servidor: python manage.py runserver

## Endpoints da API

- **Categorias:** `/api/categories/`
- **Produtos:** `/api/products/`
- **Movimentações:** `/api/movements/`

## Como acessar pelo navegador

Após rodar o comando runserver, a aplicação está rodando na porta 8000.

Interface Principal: http://127.0.0.1:8000/

API REST
Painel da API: http://127.0.0.1:8000/api/
Produtos: http://127.0.0.1:8000/api/products/
Categorias: http://127.0.0.1:8000/api/categories/
Movimentações: http://127.0.0.1:8000/api/movements/
