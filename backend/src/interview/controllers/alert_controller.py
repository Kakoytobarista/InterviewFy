from fastapi import HTTPException, APIRouter
from starlette.status import HTTP_400_BAD_REQUEST

from ..schemas.telegram_alert_schema import SendTelegramAlert
from ...alerts.telegram_alert import TelegramAlert

router = APIRouter(prefix="/alert", tags=["alert"])


@router.post("/send_alert")
async def send_alert(data: SendTelegramAlert) -> None:
    try:
        TelegramAlert().send_alert_in_chat(text=data.text)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
