using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class User
{
    public int UserID;           // ���������� ������������� ������
    public string Login;         // ����� ������
    public string PasswordHash;  // ������������ ������
    public string DateCreated;   // ���� �������� ������� (� ������� ������)
}

public class UserList
{
    public List<User> users; // ������ �������������
}

[System.Serializable]
public class Work
{
    public int WorkID;           // ���������� ������������� ������
    public int UserID;           // ������ �� ������������, ���������� ������
    public string WorkType;      // ��� ������ (��������, "3D-������", "��������")
    public string WorkContent;   // ���������� ������ � ���� ������ Base64
    public string DateAdded;     // ���� ���������� ������
    public int LikesCount;       // ���������� ������
}

[System.Serializable]
public class Avatar
{
    public int AvatarID;               // ���������� ������������� ������
    public int UserID;                 // ������ �� ������
    public int EyeColor;               // ���� ����
    public int HairStyle;              // ����� �����
    public int SkinColor;              // ���� ����
    public int Outfit;                 // ��� ������
    public Dictionary<string, string> OtherAttributes; // �������������� ��������� (JSON ��� �������)
}

[System.Serializable]
public class Room
{
    public int RoomID;                 // ���������� ������������� �������
    public int UserID;                 // ������ �� ������
    public int? Slot1WorkID;           // ID ������ � ������ ����� (nullable)
    public int? Slot2WorkID;           // ID ������ �� ������ ����� (nullable)
    public int? Slot3WorkID;           // ID ������ � ������� ����� (nullable)
    public int? Slot4WorkID;           // ID ������ � �������� ����� (nullable)
    public int? Slot5WorkID;           // ID ������ � ����� ����� (nullable)
    public int? Slot6WorkID;           // ID ������ � ������ ����� (nullable)
    public int? Slot7WorkID;           // ID ������ � ������� ����� (nullable)
    public int? Slot8WorkID;           // ID ������ � ������� ����� (nullable)
    public int? Slot9WorkID;           // ID ������ � ������� ����� (nullable)
    public int? Slot10WorkID;          // ID ������ � ������� ����� (nullable)
    public Dictionary<string, string> RoomSettings; // ��������� ������� (JSON ��� �������)
}

[System.Serializable]
public class DatabaseData
{
    public List<User> Users;          // ������ �������������
    public List<Work> Works;          // ������ �����
    public List<Avatar> Avatars;      // ������ ��������
    public List<Room> Rooms;          // ������ ������
}
