from pydantic import BaseModel


# Base schemas
class BankBase(BaseModel):
    name: str


class BranchBase(BaseModel):
    ifsc: str
    branch: str
    address: str
    city: str
    district: str
    state: str
    bank_id: int


# Response schemas with ORM mode enabled
class Bank(BankBase):
    id: int

    class Config:
        orm_mode = True


class Branch(BranchBase):
    id: int

    class Config:
        orm_mode = True
