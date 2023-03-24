from sqlalchemy import BigInteger, text, Column, Date, Integer, ForeignKeyConstraint, PrimaryKeyConstraint, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata =Base.metadata

class Reserva(Base):
    __tablename__ = 'reserva'
    __table_args__ = (
        ForeignKeyConstraint(['cpf_proprietario'], ['conta.cpf_proprietario'], ondelete='CASCADE', onupdate='RESTRICT', name='reserva_conta_fk'),
        PrimaryKeyConstraint('id_reserva', name='reserva_pk')
    )

    id_reserva = Column(Integer, primary_key=True, server_default=text("nextval('reserva_id_reserva_seq'::regclass)"))
    dt_criacao = Column(Date, nullable=False)
    titulo_reserva = Column(String(30), nullable=False)
    cpf_proprietario = Column(BigInteger, nullable=False)
    descricao_reserva = Column(String(100))

    # conta = relationship('Conta', back_populates='reserva')
    # saida = relationship('Saida', back_populates='reserva')
    # entrada = relationship('Entrada', back_populates='reserva')
