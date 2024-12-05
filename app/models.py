from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, LargeBinary, JSON
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

# Базовый класс для определения моделей
Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'

    UserID = Column(Integer, primary_key=True, autoincrement=True)  # Уникальный идентификатор игрока
    Login = Column(String(50), unique=True, nullable=False)        # Логин игрока
    PasswordHash = Column(String(255), nullable=False)              # Хэшированный пароль
    DateCreated = Column(DateTime, server_default=func.now())       # Дата создания профиля

    # Связь с работами
    works = relationship("Work", back_populates="user")

    # Связь с аватаром
    avatar = relationship("Avatar", back_populates="user", uselist=False)

    # Связь с комнатой
    room = relationship("Room", back_populates="user", uselist=False)

class Work(Base):
    __tablename__ = 'Works'

    WorkID = Column(Integer, primary_key=True, autoincrement=True)  # Уникальный идентификатор работы
    UserID = Column(Integer, ForeignKey('Users.UserID', ondelete='CASCADE'), nullable=False)  # Ссылка на пользователя
    WorkType = Column(String(50), nullable=False)                    # Тип работы
    WorkContent = Column(LargeBinary, nullable=False)                # Содержимое работы в виде бинарных данных
    DateAdded = Column(DateTime, server_default=func.now())         # Дата добавления работы
    LikesCount = Column(Integer, default=0)                          # Количество лайков

    # Связь с пользователем
    user = relationship("User", back_populates="works")

class Avatar(Base):
    __tablename__ = 'Avatars'

    AvatarID = Column(Integer, primary_key=True, autoincrement=True)  # Уникальный идентификатор аватара
    UserID = Column(Integer, ForeignKey('Users.UserID', ondelete='CASCADE'), nullable=False)  # Ссылка на пользователя
    EyeColor = Column(Integer, default=0)                            # Цвет глаз
    HairStyle = Column(Integer, default=0)                           # Стиль волос
    SkinColor = Column(Integer, default=0)                           # Цвет кожи
    Outfit = Column(Integer, default=0)                              # Тип одежды
    OtherAttributes = Column(JSON, default=None)                     # Дополнительные параметры в формате JSON

    # Связь с пользователем
    user = relationship("User", back_populates="avatar")

class Room(Base):
    __tablename__ = 'Rooms'

    RoomID = Column(Integer, primary_key=True, autoincrement=True)  # Уникальный идентификатор комнаты
    UserID = Column(Integer, ForeignKey('Users.UserID', ondelete='CASCADE'), nullable=False)  # Ссылка на пользователя
    Slot1WorkID = Column(Integer, ForeignKey('Works.WorkID', ondelete='SET NULL'), default=None)  # ID работы в первом слоте
    Slot2WorkID = Column(Integer, ForeignKey('Works.WorkID', ondelete='SET NULL'), default=None)  # ID работы во втором слоте
    Slot3WorkID = Column(Integer, ForeignKey('Works.WorkID', ondelete='SET NULL'), default=None)  # ID работы в третьем слоте
    Slot4WorkID = Column(Integer, ForeignKey('Works.WorkID', ondelete='SET NULL'), default=None)  # ID работы в четвертом слоте
    Slot5WorkID = Column(Integer, ForeignKey('Works.WorkID', ondelete='SET NULL'), default=None)  # ID работы в пятом слоте
    Slot6WorkID = Column(Integer, ForeignKey('Works.WorkID', ondelete='SET NULL'), default=None)  # ID работы в шестом слоте
    Slot7WorkID = Column(Integer, ForeignKey('Works.WorkID', ondelete='SET NULL'), default=None)  # ID работы в седьмом слоте
    Slot8WorkID = Column(Integer, ForeignKey('Works.WorkID', ondelete='SET NULL'), default=None)  # ID работы в восьмом слоте
    Slot9WorkID = Column(Integer, ForeignKey('Works.WorkID', ondelete='SET NULL'), default=None)  # ID работы в девятом слоте
    Slot10WorkID = Column(Integer, ForeignKey('Works.WorkID', ondelete='SET NULL'), default=None) # ID работы в десятом слоте
    RoomSettings = Column(JSON, default=None)  # Настройки комнаты (цвет, текстуры и т.д.)

    # Связь с пользователем
    user = relationship("User", back_populates="room")