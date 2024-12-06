from sqlalchemy.orm import Session, joinedload
from app import models, schemas


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).order_by(models.User.UserID).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, UserID: int):
    return db.query(models.User).filter(models.User.UserID == UserID).first()

def get_works_by_user_id(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return (
        db.query(models.Work)
        .filter(models.Work.UserID == user_id)
        .order_by(models.Work.WorkID)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_user_by_username(db: Session, Login: str):
    return db.query(models.User).filter(models.User.Login == Login).first()

def get_user_by_nickname(db: Session, Nickname: str):
    return db.query(models.User).filter(models.User.Nickname == Nickname).first()

def create_work(db: Session, user_id: int, work_data: schemas.WorkCreate):
    new_work = models.Work(
        UserID=user_id,
        WorkType=work_data.WorkType,
        WorkContent=work_data.WorkContent,
        LikesCount=work_data.LikesCount or 0,
    )
    db.add(new_work)
    db.commit()
    db.refresh(new_work)
    return new_work

from sqlalchemy.orm import Session
from app import models, schemas

def save_avatar(db: Session, user_id: int, avatar_data: schemas.AvatarCreate):
    avatar = db.query(models.Avatar).filter(models.Avatar.UserID == user_id).first()
    if not avatar:
        avatar = models.Avatar(
            UserID=user_id,
            EyeColor=avatar_data.EyeColor,
            HairStyle=avatar_data.HairStyle,
            SkinColor=avatar_data.SkinColor,
            Outfit=avatar_data.Outfit,
        )
        db.add(avatar)
    else:
        avatar.EyeColor = avatar_data.EyeColor
        avatar.HairStyle = avatar_data.HairStyle
        avatar.SkinColor = avatar_data.SkinColor
        avatar.Outfit = avatar_data.Outfit
    db.commit()
    db.refresh(avatar)
    return avatar
