from sqlalchemy import BigInteger, CheckConstraint, Column, Date, DateTime, Enum, ForeignKeyConstraint, Numeric, PrimaryKeyConstraint, String, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata =Base.metadata

class Meta(Base):
    __tablename__ = 'meta'
    __table_args__ = (
        ForeignKeyConstraint(['cpf_proprietario'], ['conta.cpf_proprietario'], ondelete='CASCADE', onupdate='RESTRICT', name='meta_conta_fk'),
        PrimaryKeyConstraint('id_meta', name='meta_pk')
    )

    id_meta = Column(BigInteger)
    valor_meta = Column(Numeric(9, 2), nullable=False)
    cpf_proprietario = Column(BigInteger, nullable=False)

    conta = relationship('Conta', back_populates='meta')