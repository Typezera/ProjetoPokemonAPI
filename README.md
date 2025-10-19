# 🏆 Desafio Técnico FullStack - Pokédex Digital

**Autor:** Willian Bardela da Silva

Este projeto implementa a solução de Backend (Python/Flask) para o desafio técnico FullStack da Kogui. O foco foi garantir a segurança, a persistência de dados e a arquitetura robusta, conforme os requisitos propostos.

---

## 🚀 1. Setup e Execução (Docker Compose)

O projeto está totalmente containerizado. Basta ter o Docker e o Docker Compose instalados.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/Typezera/ProjetoPokemonAPI.git](https://github.com/Typezera/ProjetoPokemonAPI.git)
    cd ProjetoPokemonAPI
    ```

2.  **Construir e Iniciar os Contêineres:**
    Este comando irá construir a imagem, instalar as dependências e iniciar o Flask na porta 5000.
    ```bash
    docker-compose up --build
    ```

3.  **Acesso:** O servidor estará acessível em `http://127.0.0.1:5000/`.

---

## ✅ 2. Tecnologias e Arquitetura

* **Backend:** Python 3.12 (Flask)
* **Banco de Dados:** SQLite (SQLAlchemy ORM)
* **Segurança:** JSON Web Token (JWT) para autenticação.
* **Arquitetura:** Camadas (Controllers, Services, Entities) para separação de responsabilidades.

## 🔑 3. Rotas Essenciais e Funcionais

Os seguintes *endpoints* foram implementados e estão operacionais:

| Método | Endpoint | Descrição | Status |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/users/register` | Cria um novo usuário. | **OK** |
| `POST` | `/api/users/login` | Autentica e retorna o **Token JWT**. | **OK** |
| `GET` | `/api/users/` | Trás todos os usuários cadastrados no sistema. | **OK** | 
| `GET` | `/api/pokemons` | Lista Pokémons iniciais (via PokéAPI). | **OK** |
| `GET` | `/api/pokemons/name/` | Procura um Pokemon Pelo nome (via PokéAPI). | **OK** |
| `POST` | `/api/pokemons/favorite` | Adiciona um Pokémon à lista de favoritos do usuário. | **OK** |
| `GET` | `/api/pokemons/favorites` | Lista os Pokémons favoritos do usuário. | **OK** |

---

## ⚠️ 4. Pendências e Justificativa

Devido à alta complexidade do mapeamento ORM (SQLAlchemy) e à urgência de conciliar o projeto com exames acadêmicos e trabalho, o tempo de estabilização final foi limitado.

* **Lógica de Negócio (Lógica Correta, Execução Instável):** Os *endpoints* para **`DELETE /favorite/{id}`** e **`POST /battle_team`** contêm a lógica de exclusão e a regra de limite de 6 Pokémons, mas falharam em *runtime* no teste final devido a problemas de *binding* com o banco de dados. A lógica para o limite está presente nos *services*.
* **Front-End:** A construção do Front-End (Angular) não foi iniciada.

**O foco principal foi garantir que a base, a segurança (JWT) e a persistência de dados (CRUD) estivessem sólidas.**
