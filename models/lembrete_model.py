from sqlalchemy import BigInteger, text, Column, Date, Integer, ForeignKeyConstraint, PrimaryKeyConstraint, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata =Base.metadata

class Lembrete(Base):
    __tablename__ = 'lembrete'
    __table_args__ = (
        ForeignKeyConstraint(['cpf_proprietario'], ['conta.cpf_proprietario'], ondelete='CASCADE', onupdate='RESTRICT', name='lembrete_conta_fk'),
        PrimaryKeyConstraint('id_lembrete', name='lembrete_pk')
    )

    id_lembrete = Column(Integer, primary_key=True, server_default=text("nextval('lembrete_id_lembrete_seq'::regclass)"))
    dt_lembrete = Column(Date, nullable=False)
    titulo_lembrete = Column(String(30), nullable=False)
    cpf_proprietario = Column(BigInteger, nullable=False)

    #conta = relationship('Conta', back_populates='lembrete')