from models.conta_model import Conta
from schemas.conta_schema import ContaSchema

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

class ContaRepo:
    @staticmethod
    def get_all(db:Session):
        try:
            contas = db.query(Conta).all()
        except Exception as err:
            raise HTTPException(
                detail=err,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        if not contas:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        return contas

    @staticmethod
    def create(nova_conta: ContaSchema, db: Session):
        try:
            conta = Conta(
                cpf_proprietario=nova_conta.cpf_proprietario,
                nome_proprietario=nova_conta.nome_proprietario,
                dt_nasc_proprietario=nova_conta.dt_nasc_proprietario,
                email=nova_conta.email,
                senha=nova_conta.senha,
                telefone=nova_conta.telefone
            )
            db.add(conta)
            db.commit()
        except Exception as err:
            raise HTTPException(
                detail=err,
                status_code=status.HTTP_400_BAD_REQUEST
            )

        return conta
        
    @staticmethod
    def destroy(cpf:int ,db:Session):
        try:
            deletar_conta = db.query(Conta).filter(Conta.cpf_proprietario == cpf).first()
            nome_proprietario = ''
            if deletar_conta:
                nome_proprietario = deletar_conta.nome_proprietario
                db.delete(deletar_conta)
                db.commit()
        except Exception as err:
            raise HTTPException(
                detail=err,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        if not deletar_conta:
            raise HTTPException(
                detail=f'A conta com cpf:{cpf} não foi encontrada',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return {
            "msg":f'A conta do {nome_proprietario} foi deletada com succeso'
        }
        