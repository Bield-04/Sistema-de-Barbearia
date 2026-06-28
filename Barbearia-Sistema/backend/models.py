from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
import datetime

# 1. Tabela de Clientes e Agendamentos
class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    nome_cliente = Column(String, nullable=False)
    telefone = Column(String, nullable=True)
    servico = Column(String, nullable=False)  # Ex: "Cabelo", "Barba"
    data_hora = Column(DateTime, nullable=False)
    status = Column(String, default="Pendente") # Pendente, Confirmado, Finalizado


# 2. Tabela opcional de Serviços (caso o barbeiro queira mudar os preços depois)
class Servico(Base):
    __tablename__ = "servicos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False) # Ex: "Corte Degradê"
    preco = Column(Float, nullable=False)