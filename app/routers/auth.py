from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import hashlib
from app import schemas, models, crud
from app.database import get_db

router = APIRouter()


@router.post("/register/", response_model=schemas.UserLoginResponse)
def reg_users(user_data: schemas.UserRegistration, db: Session = Depends(get_db)):
    try:
        hashed_password = hashlib.sha256(user_data.PasswordHash.encode("utf-8")).hexdigest()

        existing_user = crud.get_user_by_username(db, Login=user_data.Login)
        existing_nick = crud.get_user_by_nickname(db, Nickname=user_data.Nickname)

        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        if existing_nick:
            raise HTTPException(status_code=400, detail="Nickname already exists")

        new_user = models.User(
            Login=user_data.Login,
            Nickname=user_data.Nickname,
            PasswordHash=hashed_password,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        new_room = models.Room(
            UserID=new_user.UserID,
        )
        db.add(new_room)
        db.commit()

        return schemas.UserLoginResponse(
            UserID=new_user.UserID,
            Login=new_user.Login,
            Nickname=new_user.Nickname,
            RoomID=new_room.RoomID
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/login/", response_model=schemas.UserLoginResponse)
def login_user(user_data: schemas.UserLoginRequest, db: Session = Depends(get_db)):
    try:
        user = crud.get_user_by_username(db, Login=user_data.Login)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid login or password")

        hashed_password = hashlib.sha256(user_data.Password.encode("utf-8")).hexdigest()
        if user.PasswordHash != hashed_password:
            raise HTTPException(status_code=401, detail="Invalid login or password")

        room = db.query(models.Room).filter(models.Room.UserID == user.UserID).first()
        if not room:
            new_room = models.Room(
                UserID=user.UserID,
            )
            db.add(new_room)
            db.commit()

        return schemas.UserLoginResponse(UserID=user.UserID, Login=user.Login, Nickname=user.Nickname, RoomID=room.RoomID)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
