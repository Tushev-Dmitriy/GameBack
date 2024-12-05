from sqlalchemy.orm import Session
from .models import User, Work, Avatar, Room

def create_user(db: Session, login: str, password: str):
    db_user = User(Login=login, PasswordHash=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_login(db: Session, login: str):
    return db.query(User).filter(User.Login == login).first()

def create_work(db: Session, user_id: int, work_type: str, content: bytes):
    db_work = Work(UserID=user_id, WorkType=work_type, WorkContent=content)
    db.add(db_work)
    db.commit()
    db.refresh(db_work)
    return db_work
