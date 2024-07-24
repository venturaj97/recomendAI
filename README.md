# RecomendAI

RecomendAI é um projeto de sistema de recomendação de filmes e séries utilizando FastAPI e Pydantic. O objetivo é criar uma API que permita aos usuários gerenciar filmes e avaliações, e obter recomendações baseadas em suas preferências.

## Funcionalidades

- **Cadastro de Usuários**: Permite criar novos usuários.
- **Autenticação**: Geração e validação de tokens JWT para autenticação.
- **Gerenciamento de Filmes**: Criação, leitura, atualização e exclusão de filmes.
- **Gerenciamento de Avaliações**: Criação, leitura, atualização e exclusão de avaliações.
- **Recomendações**: Geração de recomendações de filmes com base nas avaliações.

## Tecnologias Utilizadas

- **FastAPI**: Framework para a construção da API.
- **Pydantic**: Validação e configuração de dados.
- **SQLModel**: ORM para interações com o banco de dados.
- **Passlib**: Biblioteca para hashing de senhas.
- **PyJWT**: Biblioteca para manipulação de tokens JWT.
- **Uvicorn**: Servidor ASGI para execução do FastAPI.

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/recomendAI.git
cd recomendAI
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
