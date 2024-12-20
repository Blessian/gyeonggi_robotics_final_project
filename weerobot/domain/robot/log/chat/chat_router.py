from typing import Any, List, Set, Dict, Tuple, Iterable, Callable, Optional, Union, cast

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_session
from domain.robot.log.chat import chat_schema, chat_crud


router: APIRouter = APIRouter(prefix="/weerobot/api/robot/log/chat")

@router.post("/")
def create_cctv(chat_log: chat_schema.ChatLogCreate, session: Session=Depends(get_session)) -> None:
    chat_crud.create_log(session, chat_log)

@router.get("/", response_model=List[chat_schema.ChatLog])
def read_chats(session: Session=Depends(get_session)) -> List[chat_schema.ChatLog]:
    return chat_crud.read_chats(session)

@router.get("/{robot_id}", response_model=List[chat_schema.ChatLog])
def read_log_chats(robot_id: int, session: Session=Depends(get_session)) -> List[chat_schema.ChatLog]:
    return chat_crud.read_log_chats(session, robot_id)