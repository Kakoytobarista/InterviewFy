from pydantic import BaseModel


class SendTelegramAlert(BaseModel):
    text: str
