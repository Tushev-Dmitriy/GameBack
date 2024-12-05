from sqlalchemy.orm import Session
from app import models

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).order_by(models.User.UserID).offset(skip).limit(limit).all()

def get_works(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Work).offset(skip).limit(limit).all()

def get_avatars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Avatar).offset(skip).limit(limit).all()

def get_rooms(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Room).offset(skip).limit(limit).all()

def get_user_by_username(db: Session, Login: str):
    return db.query(models.User).filter(models.User.Login == Login).first()