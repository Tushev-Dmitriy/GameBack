import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, database, schemas
from pydantic import BaseModel
import hashlib
from datetime import datetime

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000)

# Dependency для получения сессии базы данных
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        users = crud.get_users(db, skip=skip, limit=limit)
        if not users:
            return []
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/works/", response_model=list[schemas.Work])
def read_works(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Получить список работ.
    """
    works = crud.get_works(db, skip=skip, limit=limit)
    return works

@app.get("/avatars/", response_model=list[schemas.Avatar])
def read_avatars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Получить список аватаров.
    """
    avatars = crud.get_avatars(db, skip=skip, limit=limit)
    return avatars

@app.get("/rooms/", response_model=list[schemas.Room])
def read_rooms(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Получить список комнат.
    """
    rooms = crud.get_rooms(db, skip=skip, limit=limit)
    return rooms

class UserRegistration(BaseModel):
    Login: str
    PasswordHash: str

class UserResponse(BaseModel):
    Login: str

    class Config:
        from_attributes = True

@app.post("/register/", response_model=schemas.UserLoginResponse)
def reg_users(user_data: UserRegistration, db: Session = Depends(get_db)):
    try:
        # Хэширование пароля
        hashed_password = hashlib.sha256(user_data.PasswordHash.encode('utf-8')).hexdigest()

        # Проверка на существование пользователя
        existing_user = crud.get_user_by_username(db, Login=user_data.Login)
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        # Создание нового пользователя
        new_user = models.User(
            Login=user_data.Login,
            PasswordHash=hashed_password,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # Возвращаем только логин
        return schemas.UserLoginResponse(Login=new_user.Login)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
