using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class User
{
    public int UserID;           // Уникальный идентификатор игрока
    public string Login;         // Логин игрока
    public string PasswordHash;  // Хэшированный пароль
    public string DateCreated;   // Дата создания профиля (в формате строки)
}

public class UserList
{
    public List<User> users; // Список пользователей
}

[System.Serializable]
public class Work
{
    public int WorkID;           // Уникальный идентификатор работы
    public int UserID;           // Ссылка на пользователя, создавшего работу
    public string WorkType;      // Тип работы (например, "3D-модель", "картинка")
    public string WorkContent;   // Содержимое работы в виде строки Base64
    public string DateAdded;     // Дата добавления работы
    public int LikesCount;       // Количество лайков
}

[System.Serializable]
public class Avatar
{
    public int AvatarID;               // Уникальный идентификатор записи
    public int UserID;                 // Ссылка на игрока
    public int EyeColor;               // Цвет глаз
    public int HairStyle;              // Стиль волос
    public int SkinColor;              // Цвет кожи
    public int Outfit;                 // Тип одежды
    public Dictionary<string, string> OtherAttributes; // Дополнительные параметры (JSON как словарь)
}

[System.Serializable]
public class Room
{
    public int RoomID;                 // Уникальный идентификатор комнаты
    public int UserID;                 // Ссылка на игрока
    public int? Slot1WorkID;           // ID работы в первом слоте (nullable)
    public int? Slot2WorkID;           // ID работы во втором слоте (nullable)
    public int? Slot3WorkID;           // ID работы в третьем слоте (nullable)
    public int? Slot4WorkID;           // ID работы в четвёртом слоте (nullable)
    public int? Slot5WorkID;           // ID работы в пятом слоте (nullable)
    public int? Slot6WorkID;           // ID работы в шестом слоте (nullable)
    public int? Slot7WorkID;           // ID работы в седьмом слоте (nullable)
    public int? Slot8WorkID;           // ID работы в восьмом слоте (nullable)
    public int? Slot9WorkID;           // ID работы в девятом слоте (nullable)
    public int? Slot10WorkID;          // ID работы в десятом слоте (nullable)
    public Dictionary<string, string> RoomSettings; // Настройки комнаты (JSON как словарь)
}

[System.Serializable]
public class DatabaseData
{
    public List<User> Users;          // Список пользователей
    public List<Work> Works;          // Список работ
    public List<Avatar> Avatars;      // Список аватаров
    public List<Room> Rooms;          // Список комнат
}
