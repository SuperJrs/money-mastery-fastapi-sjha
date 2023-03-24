from models.meta_model import Meta
from schemas.meta_schema import MetaSchema, MetaSchemaOptional

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

class MetaRepo:
    @staticmethod
    def create(nova_meta: MetaSchema, db: Session):
        try:
            meta = Meta(
                valor_meta=nova_meta.valor_meta,
                cpf_proprietario=nova_meta.cpf_proprietario
            )
            db.add(meta)
            db.commit()
        except Exception as err:
              raise HTTPException(
                detail=str(err),
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return meta
    
    @staticmethod
    def destroy(cpf:int, id_meta:int, db:Session):
        try:
            deletar_meta = db.query(Meta).filter(Meta.cpf_proprietario==cpf, Meta.id_meta==id_meta).first()
            numero_meta = ''
            if deletar_meta:
                numero_meta = deletar_meta.id_meta
                db.delete(deletar_meta)
                db.commit()
        except Exception as err:
            raise HTTPException(
                detail=str(err),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
             )
        if not deletar_meta:
            raise HTTPException(
                detail=f'A meta:{id_meta} não foi encontrada',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return {
            "msg":f'A meta {numero_meta} foi deletada com succeso'
        } 
    
    @staticmethod
    def update(cpf:int, id_meta:int, novo_valor:MetaSchemaOptional, db:Session):
        try:
            meta_alterada: Meta = db.query(Meta).filter(Meta.cpf_proprietario==cpf, Meta.id_meta==id_meta).first()
            if meta_alterada:
                print("chego")
                meta_alterada.valor_meta = novo_valor.valor_meta
                db.commit()
        except Exception as err:
            raise HTTPException(
                detail=str(err),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        if not meta_alterada:
            raise HTTPException(
                detail=f'A meta não foi encontrada',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return meta_alterada
    
    @staticmethod
    def get_all_by_cpf(cpf:int, db:Session):
        try:
              meta_cpf = db.query(Meta).filter(Meta.cpf_proprietario==cpf).all()

        except Exception as err:
              raise HTTPException(
                detail=err,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        if not meta_cpf:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        return meta_cpf

