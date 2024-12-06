import uvicorn
import database
import schemas
import crud

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from app.routers import auth, works, users

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(works.router, prefix="/works", tags=["works"])
app.include_router(users.router, prefix="/user", tags=["user"])

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000)

@app.get("/users/", response_model=List[schemas.UserSchema])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    try:
        users = crud.get_users(db=db, skip=skip, limit=limit)
        if not users:
            raise HTTPException(status_code=404, detail="No users found")
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))