from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas
from app.database import get_db
from app.models import Bank, Branch

router = APIRouter(
    tags=["Branches"]
)


@router.get("/banks/{bank_id}/branches", response_model=List[schemas.Branch])
def get_branches_by_bank(bank_id: int, db: Session = Depends(get_db)):
    # Check if the bank exists
    bank = db.query(Bank).filter(Bank.id == bank_id).first()
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")
    
    # Return all branches for that bank
    branches = db.query(Branch).filter(Branch.bank_id == bank_id).all()
    return branches


@router.get("/branches/{ifsc}", response_model=schemas.Branch)
def get_branch_by_ifsc(ifsc: str, db: Session = Depends(get_db)):
    # Fetch branch by IFSC
    branch = db.query(Branch).filter(Branch.ifsc == ifsc).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    
    return branch
