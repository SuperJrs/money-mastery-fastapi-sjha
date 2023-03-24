from fastapi import APIRouter, Depends, HTTPException, status
from models.conta_model import Conta
from core.deps import get_session
from schemas.conta_schema import ContaSchema, ContaSchemaUpdate
from repository.conta_repo import ContaRepo



router = APIRouter(prefix="/conta")
repo = ContaRepo()

@router.get("/", response_model=list[ContaSchema])
def obter_contas(db=Depends(get_session)):
    return repo.get_all(db)

@router.post("/", response_model=ContaSchema, status_code=status.HTTP_201_CREATED)
def adicionar_nova_conta(nova_conta: ContaSchema, db = Depends(get_session)):
    return repo.create(nova_conta, db)

@router.delete("/{cpf}", status_code=status.HTTP_202_ACCEPTED)
def deletar_conta(cpf: int, db=Depends(get_session)):
    return repo.destroy(cpf, db)

@router.get("/{cpf}", response_model=ContaSchema)
def obter_conta_cpf(cpf: int, db=Depends(get_session)):
    return repo.get_by_cpf(cpf, db)

@router.put("/{cpf}", response_model=ContaSchema)
def atulizar_conta(cpf:int, dados_conta: ContaSchemaUpdate, db=Depends(get_session)):
    return repo.update(cpf, dados_conta, db)