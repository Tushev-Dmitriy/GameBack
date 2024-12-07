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

@router.post("/{work_id}/moderate/")
def set_work_moderated(work_id: int, db: Session = Depends(get_db)):
    try:
        work = db.query(models.Work).filter(models.Work.WorkID == work_id).first()
        if not work:
            raise HTTPException(status_code=404, detail="Work not found")

        work.IsModerated = True
        db.commit()
        db.refresh(work)

        return {"message": f"Work with ID {work_id} is now moderated", "work": work.WorkID}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{user_id}/{work_id}/delete")
def delete_work(user_id: int, work_id: int, db: Session = Depends(get_db)):
    try:
        work = db.query(models.Work).filter(models.Work.WorkID == work_id).first()
        if not work:
            raise HTTPException(status_code=404, detail="Work not found")

        if work.UserID != user_id:
            raise HTTPException(status_code=403, detail="You do not have permission to delete this work")

        db.delete(work)
        db.commit()

        return {"message": f"Work with ID {work_id} has been successfully deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

