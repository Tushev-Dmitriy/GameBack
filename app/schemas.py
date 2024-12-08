import base64

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class UserLoginResponse(BaseModel):
    UserID: int
    Login: str
    Nickname: str
    RoomID: int

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
    WorkTitle: str
    WorkContent: bytes
    LikesCount: int = 0

class WorkSchema(BaseModel):
    WorkID: int
    WorkType: str
    WorkTitle: str
    WorkContent: str
    DateAdded: datetime
    LikesCount: int
    IsModerated: bool
    class Config:
        from_attributes = True


class AvatarSchema(BaseModel):
    AvatarID: int
    EyeColor: int
    HairStyle: int
    SkinColor: int
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
    Slot1WorkID: Optional[int]
    Slot2WorkID: Optional[int]
    Slot3WorkID: Optional[int]
    Slot4WorkID: Optional[int]
    Slot5WorkID: Optional[int]
    Slot6WorkID: Optional[int]
    Slot7WorkID: Optional[int]
    Slot8WorkID: Optional[int]
    Slot9WorkID: Optional[int]
    Slot10WorkID: Optional[int]

    class Config:
        from_attributes = True

class RoomWorksResponse(BaseModel):
    RoomID: int
    Works: List[WorkSchema]

class AddWorkRequest(BaseModel):
    work_id: int
    user_id: int
