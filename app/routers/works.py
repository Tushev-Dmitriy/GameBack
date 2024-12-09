from fastapi import APIRouter, Depends, HTTPException, Form, UploadFile
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models, crud
from app.database import get_db

router = APIRouter()

@router.get("/{user_id}", response_model=List[schemas.AllWorkSchema])
def get_user_works(user_id: int, skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
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


@router.post("/{user_id}/add", response_model=dict)
def add_work(
    user_id: int,
    work_type: str = Form(...),
    work_title: str = Form(...),
    file: UploadFile = Form(...),
    db: Session = Depends(get_db)
):
    try:
        file_content = file.file.read()

        new_work = models.Work(
            UserID=user_id,
            WorkType=work_type,
            WorkContent=file_content,
            WorkTitle=work_title,
        )
        db.add(new_work)
        db.commit()
        db.refresh(new_work)

        return {"message": "Work added successfully", "WorkID": new_work.WorkID}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{work_id}/moderate")
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


@router.get("/top/", response_model=list[schemas.WorkSchema])
def get_top_works(days: int = 1, limit: int = 5, db: Session = Depends(get_db)):
    try:
        top_works = crud.get_top_works(db, days=days, limit=limit)
        if not top_works:
            raise HTTPException(status_code=404, detail="No works found")
        return top_works
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{work_id}/like")
def like_work(work_id: int, db: Session = Depends(get_db)):
    try:
        work = db.query(models.Work).filter(models.Work.WorkID == work_id).first()
        if not work:
            raise HTTPException(status_code=404, detail="Work not found")

        if not work.IsModerated:
            raise HTTPException(status_code=403, detail="Cannot like a work that is not moderated")

        work.LikesCount += 1
        db.commit()
        db.refresh(work)

        return {"WorkID": work.WorkID, "LikesCount": work.LikesCount}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{work_id}/validate/{expected_type}")
def validate_work_type(work_id: int, expected_type: str, db: Session = Depends(get_db)):
    try:
        work = db.query(models.Work).filter(models.Work.WorkID == work_id).first()
        if not work:
            raise HTTPException(status_code=404, detail="Work not found")

        if work.WorkType.lower() != expected_type.lower():
            raise HTTPException(status_code=400, detail=f"Work type mismatch. Expected {expected_type}, got {work.WorkType}")

        return {"message": "Work type is valid"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
