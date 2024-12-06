from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models, crud
from app.database import get_db

router = APIRouter()

@router.post("/{user_id}/avatar", response_model=schemas.AvatarSchema)
def save_user_avatar(user_id: int, avatar_data: schemas.AvatarCreate, db: Session = Depends(get_db)):
    try:
        user = crud.get_user_by_id(db, UserID=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        updated_avatar = crud.save_avatar(db, user_id=user_id, avatar_data=avatar_data)
        return updated_avatar
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{user_id}/avatar", response_model=schemas.AvatarSchema)
def get_avatar(user_id: int, db: Session = Depends(get_db)):
    try:
        avatar = db.query(models.Avatar).filter(models.Avatar.UserID == user_id).first()
        if not avatar:
            raise HTTPException(status_code=404, detail="Avatar not found")

        return avatar
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
