from pydantic import BaseModel


class AppSettings(BaseModel):
    log_level: str
    host: str
    port: int
    uvicorn_max_workers: int
