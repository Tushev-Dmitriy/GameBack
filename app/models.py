from datetime import datetime

from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text,
    LargeBinary,
    Boolean
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database import engine
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    __table_args__ = {"autoload_with": engine}

    UserID = Column(Integer, primary_key=True)
    Login = Column(String(50))
    Nickname = Column(String(50))
    PasswordHash = Column(String(255))
    DateCreated = Column(DateTime, server_default=func.now())

    works = relationship("Work", back_populates="user")
    avatar = relationship("Avatar", uselist=False, back_populates="user")
    rooms = relationship("Room", back_populates="user")



class Work(Base):
    __tablename__ = "Works"
    __table_args__ = {"autoload_with": engine}

    WorkID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("Users.UserID"), nullable=False)
    WorkType = Column(String, nullable=False)
    WorkTitle = Column(String, nullable=True)
    WorkContent = Column(LargeBinary, nullable=False)
    DateAdded = Column(DateTime, default=datetime.utcnow)
    LikesCount = Column(Integer, default=0)
    IsModerated = Column(Boolean, default=False)

    user = relationship("User", back_populates="works")
    rooms = relationship(
        "Room",
        primaryjoin="or_(Room.Slot1WorkID == Work.WorkID, "
                    "Room.Slot2WorkID == Work.WorkID, "
                    "Room.Slot3WorkID == Work.WorkID, "
                    "Room.Slot4WorkID == Work.WorkID, "
                    "Room.Slot5WorkID == Work.WorkID, "
                    "Room.Slot6WorkID == Work.WorkID, "
                    "Room.Slot7WorkID == Work.WorkID, "
                    "Room.Slot8WorkID == Work.WorkID, "
                    "Room.Slot9WorkID == Work.WorkID, "
                    "Room.Slot10WorkID == Work.WorkID)",
    )

    def get_work_content_as_string(self):
        return self.WorkContent.decode('utf-8')

class Avatar(Base):
    __tablename__ = "Avatars"
    __table_args__ = {"autoload_with": engine}

    AvatarID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey("Users.UserID"))
    EyeColor = Column(Integer)
    HairStyle = Column(Integer)
    SkinColor = Column(Integer)
    Outfit = Column(Integer)

    user = relationship("User", back_populates="avatar")


class Room(Base):
    __tablename__ = "Rooms"
    __table_args__ = {"autoload_with": engine}

    RoomID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey("Users.UserID"))
    Slot1WorkID = Column(Integer, ForeignKey("Works.WorkID"))
    Slot2WorkID = Column(Integer, ForeignKey("Works.WorkID"))
    Slot3WorkID = Column(Integer, ForeignKey("Works.WorkID"))
    Slot4WorkID = Column(Integer, ForeignKey("Works.WorkID"))
    Slot5WorkID = Column(Integer, ForeignKey("Works.WorkID"))
    Slot6WorkID = Column(Integer, ForeignKey("Works.WorkID"))
    Slot7WorkID = Column(Integer, ForeignKey("Works.WorkID"))
    Slot8WorkID = Column(Integer, ForeignKey("Works.WorkID"))
    Slot9WorkID = Column(Integer, ForeignKey("Works.WorkID"))
    Slot10WorkID = Column(Integer, ForeignKey("Works.WorkID"))

    user = relationship("User", back_populates="rooms")

    slot1_work = relationship(
        "Work",
        foreign_keys=[Slot1WorkID],
        back_populates="rooms",
        lazy="joined",
        overlaps="rooms"
    )
    slot2_work = relationship(
        "Work",
        foreign_keys=[Slot2WorkID],
        lazy="joined",
        overlaps="rooms"
    )
    slot3_work = relationship(
        "Work",
        foreign_keys=[Slot3WorkID],
        lazy="joined",
        overlaps="rooms"
    )
    slot4_work = relationship(
        "Work",
        foreign_keys=[Slot4WorkID],
        lazy="joined",
        overlaps="rooms"
    )
    slot5_work = relationship(
        "Work",
        foreign_keys=[Slot5WorkID],
        lazy="joined",
        overlaps="rooms"
    )
    slot6_work = relationship(
        "Work",
        foreign_keys=[Slot6WorkID],
        lazy="joined",
        overlaps="rooms"
    )
    slot7_work = relationship(
        "Work",
        foreign_keys=[Slot7WorkID],
        lazy="joined",
        overlaps="rooms"
    )
    slot8_work = relationship(
        "Work",
        foreign_keys=[Slot8WorkID],
        lazy="joined",
        overlaps="rooms"
    )
    slot9_work = relationship(
        "Work",
        foreign_keys=[Slot9WorkID],
        lazy="joined",
        overlaps="rooms"
    )
    slot10_work = relationship(
        "Work",
        foreign_keys=[Slot10WorkID],
        lazy="joined",
        overlaps="rooms"
    )