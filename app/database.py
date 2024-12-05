from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Получаем строку подключения
DATABASE_URL = os.getenv("DATABASE_URL")

# Создаем движок для подключения к базе данных
engine = create_engine(DATABASE_URL, echo=True)

# Создаем сессию для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Создание всех таблиц в базе данных
from .models import Base
Base.metadata.create_all(bind=engine)
