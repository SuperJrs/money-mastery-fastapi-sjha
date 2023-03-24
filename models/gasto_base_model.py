from sqlalchemy import BigInteger, text, Column, Integer, ForeignKeyConstraint, Numeric, PrimaryKeyConstraint, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata =Base.metadata

class GastoBase(Base):
    __tablename__ = 'gasto_base'
    __table_args__ = (
        ForeignKeyConstraint(['cpf_proprietario'], ['conta.cpf_proprietario'], ondelete='CASCADE', onupdate='RESTRICT', name='gasto_base_conta_fk'),
        PrimaryKeyConstraint('id_gasto_base', name='gasto_base_pk')
    )

    id_gasto_base = Column(Integer, primary_key=True, server_default=text("nextval('gasto_base_id_gasto_base_seq'::regclass)"))
    titulo_gasto = Column(String(30), nullable=False)
    valor_gasto = Column(Numeric(9, 2), nullable=False)
    cpf_proprietario = Column(BigInteger, nullable=False)

    # conta = relationship('Conta', back_populates='gasto_base')
