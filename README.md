# EstoquePro - Sistema de Gerenciamento de Estoque

Este é um projeto completo desenvolvido em Django e Django REST Framework para gerenciamento de estoque de loja. O projeto atende a todos os requisitos solicitados.

## Funcionalidades
- **Interface Web Premium**: Desenvolvida com HTML, CSS puro moderno (tipografia Inter, glassmorphism e Dark Mode dinâmico) integrado com Bootstrap.
- **CRUD Completo**: Cadastro, listagem, edição e exclusão de Produtos, Categorias e Movimentações com controle de quantidade.
- **Autenticação e Autorização**: Listagem de produtos é pública. As operações de manipulação (CRUD) restritas para usuários com login.
- **API REST Protegida**: Endpoints para todos os recursos com proteção por Token.

## Como Executar Localmente

1. Crie um ambiente virtual (se ainda não existir):
   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:
   - no Windows: `.\venv\Scripts\activate`
   - no Linux/Mac: `source venv/bin/activate`

3. Instale as dependências requisitadas:
   ```bash
   pip install django djangorestframework django-cors-headers
   ```

4. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário:
   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
   Acesse a aplicação no navegador em `http://127.0.0.1:8000/`.

## Endpoints da API

A API requer envio de cabeçalho `Authorization: Token <seu-token>`.

- **Token de Acesso:** `POST /api/auth/token/` (corpo: `username`, `password`)
- **Categorias:** `/api/categories/`
- **Produtos:** `/api/products/`
- **Movimentações:** `/api/movements/`

## Entrega do Projeto

Para enviar ao GitHub, basta criar um repositório vazio em sua conta do GitHub e rodar:
```bash
git remote add origin https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
git branch -M main
git push -u origin main
```
O link do seu repositório público deverá ser enviado na entrega do trabalho.
