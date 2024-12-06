from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class UserLoginResponse(BaseModel):
    UserID: int
    Login: str
    Nickname: str

    class Config:
        from_attributes = True

class UserRegistration(BaseModel):
    Login: str
    Nickname: str
    PasswordHash: str

    class Config:
        from_attributes = True


class UserLoginRequest(BaseModel):
    Login: str
    Password: str

    class Config:
        from_attributes = True

class WorkCreate(BaseModel):
    WorkType: str
    WorkContent: bytes
    LikesCount: int = 0

class WorkSchema(BaseModel):
    WorkID: int
    UserID: int
    WorkType: str
    DateAdded: datetime
    LikesCount: int

    class Config:
        from_attributes = True


class AvatarSchema(BaseModel):
    AvatarID: int
    EyeColor: int
    HairStyle: int
    Outfit: int

    class Config:
        from_attributes = True

class AvatarCreate(BaseModel):
    EyeColor: int
    HairStyle: int
    SkinColor: int
    Outfit: int

class UserSchema(BaseModel):
    UserID: int
    Login: str
    DateCreated: datetime
    works: Optional[List[WorkSchema]] = []
    avatar: Optional[AvatarSchema] = None

    class Config:
        from_attributes = True

class RoomSchema(BaseModel):
    RoomID: int
    Slot1WorkID: Optional[int] = None
    Slot2WorkID: Optional[int] = None
    Slot3WorkID: Optional[int] = None
    Slot4WorkID: Optional[int] = None
    Slot5WorkID: Optional[int] = None
    Slot6WorkID: Optional[int] = None
    Slot7WorkID: Optional[int] = None
    Slot8WorkID: Optional[int] = None
    Slot9WorkID: Optional[int] = None
    Slot10WorkID: Optional[int] = None
    RoomSettings: Optional[dict] = None

    class Config:
        from_attributes = True