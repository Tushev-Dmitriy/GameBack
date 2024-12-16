from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime, timedelta
import base64

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).order_by(models.User.UserID).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, UserID: int):
    return db.query(models.User).filter(models.User.UserID == UserID).first()


def get_works_by_user_id(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    works = (
        db.query(models.Work)
        .filter(models.Work.UserID == user_id)
        .order_by(models.Work.WorkID)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return [schemas.AllWorkSchema.from_orm(work) for work in works]

import base64

def get_top_works(db: Session, days: int = 1, limit: int = 5):
    from datetime import datetime, timedelta
    recent_date = datetime.utcnow() - timedelta(days=days)

    works = (
        db.query(models.Work)
        .filter(
            models.Work.DateAdded >= recent_date,
            models.Work.IsModerated == True
        )
        .order_by(models.Work.LikesCount.desc())
        .limit(limit)
        .all()
    )

    for work in works:
        if work.WorkContent:
            work.WorkContent = base64.b64encode(work.WorkContent).decode('utf-8')

    return works


def get_user_by_username(db: Session, Login: str):
    return db.query(models.User).filter(models.User.Login == Login).first()

def get_user_by_nickname(db: Session, Nickname: str):
    return db.query(models.User).filter(models.User.Nickname == Nickname).first()

def create_work(db: Session, user_id: int, work_data: schemas.WorkCreate):
    new_work = models.Work(
        UserID=user_id,
        WorkType=work_data.WorkType,
        WorkTitle=work_data.WorkTitle,
        WorkContent=work_data.WorkContent,
        LikesCount=work_data.LikesCount or 0,
    )
    db.add(new_work)
    db.commit()
    db.refresh(new_work)
    return new_work

def save_avatar(db: Session, user_id: int, avatar_data: schemas.AvatarCreate):
    avatar = db.query(models.Avatar).filter(models.Avatar.UserID == user_id).first()
    if not avatar:
        avatar = models.Avatar(
            UserID=user_id,
            HairStyle=avatar_data.HairStyle,
            Gender=avatar_data.Gender,
            OutfitTop=avatar_data.OutfitTop,
            OutfitDown=avatar_data.OutfitDown,
        )
        db.add(avatar)
    else:
        avatar.HairStyle = avatar_data.HairStyle
        avatar.Gender = avatar_data.Gender
        avatar.OutfitTop = avatar_data.OutfitTop
        avatar.OutfitDown = avatar_data.OutfitDown
    db.commit()
    db.refresh(avatar)
    return avatar
