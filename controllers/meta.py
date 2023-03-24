from fastapi import APIRouter, Depends, HTTPException, status
from models.meta_model import Meta
from core.deps import get_session
from schemas.meta_schema import MetaSchema, MetaSchemaOptional, MetaSchemaAll
from repository.meta_repo import MetaRepo

router = APIRouter(prefix="/meta")
repo = MetaRepo()

@router.post("/", response_model=MetaSchema, status_code=status.HTTP_201_CREATED)
def adicionar_nova_meta(nova_meta: MetaSchema, db = Depends(get_session)):
    return repo.create(nova_meta, db)

@router.delete("/{cpf}/{id_meta}", status_code=status.HTTP_202_ACCEPTED)
def deletar_meta( cpf: int, id_meta:int, db = Depends(get_session)):
    return repo.destroy(cpf,id_meta, db)

@router.put("/{cpf}/{id_meta}", response_model=MetaSchema)
def update_meta( cpf: int, id_meta:int, novo_valor:MetaSchemaOptional, db = Depends(get_session)):
    return repo.update(cpf,id_meta, novo_valor,db)

@router.get("/{cpf}", response_model=list[MetaSchemaAll])
def obter_metas_cpf( cpf: int,db = Depends(get_session)):
    return repo.get_all_by_cpf(cpf, db)