from sqlalchemy import BigInteger, Integer, Column, text, DateTime, Enum, ForeignKeyConstraint, Numeric, PrimaryKeyConstraint, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata =Base.metadata

class Saida(Base):
    __tablename__ = 'saida'
    __table_args__ = (
        ForeignKeyConstraint(['cpf_proprietario'], ['conta.cpf_proprietario'], ondelete='CASCADE', onupdate='RESTRICT', name='saida_conta_fk'),
        ForeignKeyConstraint(['id_reserva'], ['reserva.id_reserva'], ondelete='RESTRICT', onupdate='CASCADE', name='saida_reserva_fk'),
        PrimaryKeyConstraint('id_saida', name='saida_pk')
    )

    id_saida = Column(Integer, primary_key=True, server_default=text("nextval('meta_id_meta_seq'::regclass)"))
    valor_saida = Column(Numeric(9, 2), nullable=False)
    categoria = Column(Enum('LAZER', 'ALIMENTACAO', 'SAUDE', 'MORADIA', 'TRANSPORTE', 'EDUCACAO', 'OUTRO', name='categoria'), nullable=False)
    forma_pagamento = Column(Enum('CREDITO', 'DEBITO', 'PIX', 'DINHEIRO', 'RESERVA', 'EMPRESTIMO', name='forma_pagamento'), nullable=False)
    dt_hora_saida = Column(DateTime, nullable=False)
    cpf_proprietario = Column(BigInteger, nullable=False)
    descricao_saida = Column(String(100))
    id_reserva = Column(BigInteger)

    # conta = relationship('Conta', back_populates='saida')
    # reserva = relationship('Reserva', back_populates='saida')
    # emprestimo = relationship('Emprestimo', back_populates='saida')