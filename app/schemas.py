from pydantic import BaseModel
from typing import Optional, List, Dict

class User(BaseModel):
    UserID: int
    Login: str
    DateCreated: str

    class Config:
        from_attributes = True

class UserLoginResponse(BaseModel):
    Login: str

    class Config:
        from_attributes = True

class Work(BaseModel):
    WorkID: int
    UserID: int
    WorkType: str
    WorkContent: str
    DateAdded: str
    LikesCount: int

    class Config:
        from_attributes = True

class Avatar(BaseModel):
    AvatarID: int
    UserID: int
    EyeColor: int
    HairStyle: int
    SkinColor: int
    Outfit: int
    OtherAttributes: Optional[Dict[str, str]]

    class Config:
        from_attributes = True

class Room(BaseModel):
    RoomID: int
    UserID: int
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
    RoomSettings: Optional[Dict[str, str]]

    class Config:
        from_attributes = True