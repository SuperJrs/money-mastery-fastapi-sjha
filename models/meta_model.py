from sqlalchemy import BigInteger, text, Column, Numeric, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata =Base.metadata

class Meta(Base):
    __tablename__ = 'meta'
   
    id_meta = Column(Integer(), primary_key=True, server_default=text("nextval('meta_id_meta_seq'::regclass)"))
    valor_meta = Column(Numeric(9, 2), nullable=False)
    cpf_proprietario = Column(BigInteger, nullable=False)

    #conta = relationship('Conta', back_populates='meta')