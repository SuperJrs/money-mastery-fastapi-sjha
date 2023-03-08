from fastapi import APIRouter, Depends, HTTPException, status
from models.conta_model import Conta
from core.deps import get_session
from schemas.conta_schema import ContaSchema
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

# @router.get("/{cpf}", response_model=ContaSchema)
# def obter_conta_cpf(cpf: int, db=Depends(get_session)):
#     conta_cpf = db.query(Conta).filter(Conta.cpf_proprietario == cpf).first()

#     if not conta_cpf:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f'A conta {cpf} não foi encontrada'
#         )
    
#     return conta_cpf