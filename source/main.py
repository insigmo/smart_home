import json
from pathlib import Path

import uvicorn

from smart_home.source.logger.logging_configurator import logging_configurator
from smart_home.source.settings.app_settings import AppSettings


def main():
    settings = get_config(Path(__file__).parent / "settings.json")
    logging_configurator(log_level=settings.log_level)
    uvicorn.run(
        "smart_home.application:application",
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level.lower(),
        workers=settings.uvicorn_max_workers
    )


def get_config(config_path: Path) -> AppSettings:
    with open(config_path) as config_file:
        return AppSettings(**json.load(config_file))


if __name__ == '__main__':
    main()
