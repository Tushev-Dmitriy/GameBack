import base64

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models, crud
from app.database import get_db
from datetime import datetime

router = APIRouter()

@router.post("/{room_id}/{slot_number}/add_work/", response_model=schemas.RoomSchema)
def add_work_to_room(
    room_id: int,
    slot_number: int,
    data: schemas.AddWorkRequest,
    db: Session = Depends(get_db)
):
    try:
        room = db.query(models.Room).filter(models.Room.RoomID == room_id).first()
        if not room:
            raise HTTPException(status_code=404, detail="Room not found")

        work = db.query(models.Work).filter(models.Work.WorkID == data.work_id, models.Work.UserID == data.user_id).first()
        if not work:
            raise HTTPException(status_code=403, detail="Work does not belong to the user or does not exist")

        if not work.IsModerated:
            raise HTTPException(status_code=400, detail="Work is not moderated")

        if slot_number < 1 or slot_number > 10:
            raise HTTPException(status_code=400, detail="Slot number must be between 1 and 10")

        current_slot_field = f"Slot{slot_number}WorkID"
        setattr(room, current_slot_field, data.work_id)

        room.NeedModeration = False

        db.commit()
        db.refresh(room)

        return schemas.RoomSchema(
            RoomID=room.RoomID,
            Slot1WorkID=room.Slot1WorkID,
            Slot2WorkID=room.Slot2WorkID,
            Slot3WorkID=room.Slot3WorkID,
            Slot4WorkID=room.Slot4WorkID,
            Slot5WorkID=room.Slot5WorkID,
            Slot6WorkID=room.Slot6WorkID,
            Slot7WorkID=room.Slot7WorkID,
            Slot8WorkID=room.Slot8WorkID,
            Slot9WorkID=room.Slot9WorkID,
            Slot10WorkID=room.Slot10WorkID,
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def is_moderated_work(work_id: int, db: Session) -> bool:
    try:
        work = db.query(models.Work).filter(models.Work.WorkID == work_id).first()
        if not work:
            raise ValueError("Work not found")
        return work.IsModerated
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error checking moderation status: {str(e)}")


@router.get("/{room_id}/works/", response_model=schemas.RoomWorksResponse)
def get_room_works(room_id: int, db: Session = Depends(get_db)):
    try:
        room = db.query(models.Room).filter(models.Room.RoomID == room_id).first()
        if not room:
            raise HTTPException(status_code=404, detail="Room not found")

        # Список всех слотов
        slots = [
            room.Slot1WorkID, room.Slot2WorkID, room.Slot3WorkID, room.Slot4WorkID,
            room.Slot5WorkID, room.Slot6WorkID, room.Slot7WorkID, room.Slot8WorkID,
            room.Slot9WorkID, room.Slot10WorkID,
        ]

        # Получаем работы, соответствующие слотам
        works = db.query(models.Work).filter(models.Work.WorkID.in_([slot for slot in slots if slot is not None])).all()
        work_dict = {work.WorkID: work for work in works}

        # Формируем ответ с учетом пустых слотов
        result_works = []
        for slot_id in slots:
            if slot_id is None:
                # Заглушка для пустого слота
                result_works.append({
                    "WorkID": -1,
                    "WorkTitle": "Empty Slot",
                    "WorkType": "None",
                    "LikesCount": 0,
                    "IsModerated": False,
                    "WorkContent": "",  # Пустое содержимое для совместимости
                    "DateAdded": datetime.utcnow(),  # Отсутствие даты
                })
            else:
                work = work_dict.get(slot_id)
                if work:
                    # Преобразуем WorkContent в Base64 только если это байты
                    if isinstance(work.WorkContent, bytes):
                        work.WorkContent = base64.b64encode(work.WorkContent).decode("utf-8")
                    else:
                        work.WorkContent = ""
                    result_works.append(work)

        return schemas.RoomWorksResponse(
            RoomID=room.RoomID,
            Works=result_works
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{room_id}/{slot_number}/remove_work/", response_model=schemas.RoomSchema)
def remove_work_from_slot(
    room_id: int,
    slot_number: int,
    db: Session = Depends(get_db)
):
    try:
        room = db.query(models.Room).filter(models.Room.RoomID == room_id).first()
        if not room:
            raise HTTPException(status_code=404, detail="Room not found")

        if slot_number < 1 or slot_number > 10:
            raise HTTPException(status_code=400, detail="Slot number must be between 1 and 10")

        current_slot_field = f"Slot{slot_number}WorkID"

        if getattr(room, current_slot_field) is None:
            raise HTTPException(status_code=400, detail=f"Slot {slot_number} is already empty")

        setattr(room, current_slot_field, None)

        db.commit()
        db.refresh(room)

        return schemas.RoomSchema(
            RoomID=room.RoomID,
            Slot1WorkID=room.Slot1WorkID,
            Slot2WorkID=room.Slot2WorkID,
            Slot3WorkID=room.Slot3WorkID,
            Slot4WorkID=room.Slot4WorkID,
            Slot5WorkID=room.Slot5WorkID,
            Slot6WorkID=room.Slot6WorkID,
            Slot7WorkID=room.Slot7WorkID,
            Slot8WorkID=room.Slot8WorkID,
            Slot9WorkID=room.Slot9WorkID,
            Slot10WorkID=room.Slot10WorkID,
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
