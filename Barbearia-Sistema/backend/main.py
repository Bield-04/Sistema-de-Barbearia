from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware # <- CORRIGIDO: Import adicionado
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
import models
from database import engine, get_db

# Cria as tabelas no SQLite
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema Barbearia - Code Tech")

# Configuração do CORS para o frontend conseguir acessar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schema do Pydantic para validar os dados
class AgendamentoCreate(BaseModel):
    nome_cliente: str
    telefone: str | None = None
    servico: str
    data_hora: datetime

# --- ROTAS ---

@app.get("/")
def home():
    return {"status": "Sucesso", "mensagem": "Backend da Barbearia rodando perfeitamente!"}

@app.get("/agendamentos")
def listar_agendamentos(db: Session = Depends(get_db)):
    return db.query(models.Agendamento).all()

# CORRIGIDO: status_code alterado de 21 para 201
@app.post("/agendamentos", status_code=201)
def criar_agendamento(agendamento: AgendamentoCreate, db: Session = Depends(get_db)):
    novo_agendamento = models.Agendamento(
        nome_cliente=agendamento.nome_cliente,
        telefone=agendamento.telefone,
        servico=agendamento.servico,
        data_hora=agendamento.data_hora
    )
    
    db.add(novo_agendamento)
    db.commit()
    db.refresh(novo_agendamento)
    
    return novo_agendamento