from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Define onde o arquivo do banco de dados vai ser salvo
# O "barber.db" vai ser criado automaticamente na raiz do seu projeto
SQLALCHEMY_DATABASE_URL = "sqlite:///./barber.db"

# 2. Cria o motor (engine) do banco de dados
# O 'check_same_thread=False' é obrigatório para o SQLite funcionar bem com o FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Cria a fábrica de sessões (cada clique ou rota vai usar uma sessão para falar com o banco)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Essa classe base vai ser herdada pelos seus modelos na hora de criar as tabelas
Base = declarative_base()

# 5. Função utilitária para abrir e fechar a conexão com o banco automaticamente nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()