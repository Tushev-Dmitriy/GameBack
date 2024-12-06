from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models, crud
from app.database import get_db

router = APIRouter()

@router.get("/{user_id}", response_model=List[schemas.WorkSchema])
def get_user_works(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        user = crud.get_user_by_id(db, UserID=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        works = crud.get_works_by_user_id(db, user_id=user_id, skip=skip, limit=limit)
        if not works:
            raise HTTPException(status_code=404, detail="No works found for this user")

        return works
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{user_id}/add", response_model=schemas.WorkSchema)
def add_user_work(user_id: int, work_data: schemas.WorkCreate, db: Session = Depends(get_db)):
    try:
        user = crud.get_user_by_id(db, UserID=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        new_work = crud.create_work(db, user_id=user_id, work_data=work_data)
        return new_work
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
