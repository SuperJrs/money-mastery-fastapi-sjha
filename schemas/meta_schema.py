from pydantic import BaseModel
from typing import Optional

class MetaSchema (BaseModel):
    valor_meta: Optional[float]
    cpf_proprietario: int

    class Config:
        orm_mode = True

class MetaSchemaOptional (BaseModel):
    valor_meta: Optional[float]

    class Config:
        orm_mode = True

class MetaSchemaAll (BaseModel):
    id_meta: int
    valor_meta: Optional[float]

    class Config:
        orm_mode = True