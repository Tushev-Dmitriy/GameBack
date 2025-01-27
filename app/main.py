import uvicorn

from fastapi import FastAPI
from app.routers import auth, works, users, rooms

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(works.router, prefix="/works", tags=["works"])
app.include_router(users.router, prefix="/user", tags=["user"])
app.include_router(rooms.router, prefix="/room", tags=["room"])

@app.get("/")
def read_root():
    return {"message": "Hello, Server!"}

if __name__ == "__main__":
    ##uvicorn.run("main:app", host="0.0.0.0", port=8000)
    uvicorn.run("main:app", host="localhost", port=8000)
