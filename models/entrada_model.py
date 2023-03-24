from sqlalchemy import BigInteger, text, Column, Date, Integer, Enum, ForeignKeyConstraint, Numeric, PrimaryKeyConstraint, String, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata =Base.metadata

class Entrada(Base):
    __tablename__ = 'entrada'
    __table_args__ = (
        ForeignKeyConstraint(['cpf_proprietario'], ['conta.cpf_proprietario'], ondelete='CASCADE', onupdate='RESTRICT', name='entrada_conta_fk'),
        ForeignKeyConstraint(['id_emprestimo'], ['emprestimo.id_emprestimo'], ondelete='RESTRICT', onupdate='CASCADE', name='entrada_emprestimo_fk'),
        ForeignKeyConstraint(['id_reserva'], ['reserva.id_reserva'], ondelete='RESTRICT', onupdate='CASCADE', name='entrada_reserva_fk'),
        PrimaryKeyConstraint('id_entrada', name='entrada_pk')
    )

    id_entrada = Column(Integer, primary_key=True, server_default=text("nextval('entrada_id_entrada_seq'::regclass)"))
    valor_entrada = Column(Numeric(9, 2), nullable=False)
    origem = Column(Enum('PIX', 'SALARIO', 'EMPRESTIMO', 'RESERVA', 'OUTRO', name='origem'), nullable=False)
    dt_hora_entrada = Column(Date, nullable=False)
    cpf_proprietario = Column(BigInteger, nullable=False)
    descricao_entrada = Column(String(100))
    id_reserva = Column(BigInteger)
    id_emprestimo = Column(BigInteger)

    # conta = relationship('Conta', back_populates='entrada')
    # emprestimo = relationship('Emprestimo', back_populates='entrada')
    # reserva = relationship('Reserva', back_populates='entrada')