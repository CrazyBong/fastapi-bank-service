from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas
from app.database import get_db
from app.models import Bank

router = APIRouter(
    prefix="/banks",
    tags=["Banks"]
)


@router.get("/", response_model=List[schemas.Bank])
def get_banks(db: Session = Depends(get_db)):
    banks = db.query(Bank).all()
    return banks
