import uvicorn

from fastapi import FastAPI
from app.routers import auth, works, users, rooms

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(works.router, prefix="/works", tags=["works"])
app.include_router(users.router, prefix="/user", tags=["user"])
app.include_router(rooms.router, prefix="/room", tags=["room"])

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000)