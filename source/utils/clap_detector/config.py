from pydantic import BaseModel


class Config(BaseModel):
    exit: bool = False
    rate: int = 44100
    channels: int = 1
    chunk_size: int = 8000
    wait: float = 1.5
    clap_algorithm_value: float = 17000
    clap_count: int = 2


class PcConfig(BaseModel):
    exit: bool = False
    rate: int = 44100
    channels: int = 3
    chunk_size: int = 8000
    wait: float = 1.5
    clap_algorithm_value: float = 17000
    clap_count: int = 2
