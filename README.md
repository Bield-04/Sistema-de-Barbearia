# 🪒 Code Barber - Sistema de Gerenciamento

Um sistema moderno, minimalista e de alta performance para gerenciamento de agendamentos de barbearia. Desenvolvido com foco em arquitetura limpa, separando completamente o ecossistema de API (Backend) da interface do usuário (Frontend).

---

## 🏗️ Arquitetura do Projeto

O sistema foi componentizado seguindo as melhores práticas de mercado:

* **Frontend (GitHub Pages):** Interface SPA (Single Page Application) responsiva, estilizada com Tailwind CSS via CDN e integrada via Fetch API com o servidor.
* **Backend (FastAPI):** API RESTful robusta com validação de dados via Pydantic e documentação automática integrada (Swagger UI).
* **Banco de Dados (SQLite):** Banco relacional leve integrado através do ORM SQLAlchemy para persistência dos dados de agendamentos.

```text
📁 Barbearia-Sistema
├── 📁 backend              # Servidor ASGI FastAPI
│   ├── database.py         # Conexão com a Session do SQLite
│   ├── main.py             # Rotas, Endpoints e Middleware CORS
│   ├── models.py           # Modelos/Tabelas do Banco de Dados
│   └── requirements.txt    # Dependências do Python
├── index.html              # Interface Principal (Raiz para GitHub Pages)
├── styles.css              # Customizações extras de UI (Scrollbar)
├── app.js                  # Controladores de Requisições e Eventos JS
└── .gitignore              # Proteção de arquivos locais e venv

🛠️ Tecnologias Utilizadas
Frontend

    HTML5 (Estruturação Semântica)

    Tailwind CSS (Estilização utilitária com design Monochrome/Zinc)

    JavaScript Assíncrono (Fetch API e Manipulação de DOM)

Backend & Banco

    Python

    FastAPI (Framework web de alta performance)

    SQLAlchemy (ORM para mapeamento do banco)

    SQLite (Banco de dados local em arquivo)

    Uvicorn (Servidor de produção ASGI)

🚀 Como Executar o Projeto Localmente
1. Clonar o Repositório
Bash

git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd Barbearia-Sistema

2. Configurar e Rodar o Backend

Navegue até a pasta do servidor, crie o ambiente virtual e instale as dependências:
Bash

cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Inicie o servidor de desenvolvimento com o Uvicorn:
Bash

uvicorn main:app --reload

    O backend estará rodando ativamente em: http://127.0.0.1:8000

    Acesse a documentação interativa das rotas em: http://127.0.0.1:8000/docs

3. Executar o Frontend

Como os arquivos estão na raiz do projeto, basta abrir o arquivo index.html diretamente em qualquer navegador moderno ou utilizar uma extensão como o Live Server no VS Code.
🌐 Endpoints da API

    GET / - Rota de verificação do status da API.

    GET /agendamentos - Retorna a lista de todos os horários marcados.

    POST /agendamentos - Registra um novo agendamento no banco de dados.

        Payload esperado:
        JSON

        {
          "nome_cliente": "Gabriel",
          "telefone": "22999999999",
          "servico": "Corte Degradê",
          "data_hora": "2026-06-28T10:00:00"
        }

📝 Licença

Desenvolvido por Gabriel / Code Tech. Sinta-se livre para usar, modificar e evoluir o sistema!


---

Salva esse arquivo na raiz como `README.md`, dá o último `git push` para o GitHub e veja a mágica acontecer: a página inicial do seu repositório vai ficar com cara de projeto de empresa grande! Pronto para fechar o dia com chave de ouro?
