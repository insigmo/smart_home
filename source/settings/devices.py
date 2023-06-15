from pydantic import BaseModel


class SmartLampSettings(BaseModel):
    ip: str
    token: str
    model: str
