from typing import Union

from miio import DeviceException, Yeelight
from smart_home.source.settings.devices import SmartLampSettings


class SmartLamp:
    def __init__(self, settings: SmartLampSettings):
        self._settings = settings
        self._lamp = None
        self.connect()

    def connect(self) -> None:
        try:
            self._lamp = Yeelight(ip=self._settings.ip, token=self._settings.token)
        except DeviceException:
            raise Exception(f"Yeelight device {self._settings.ip=} is not responding.")

    def _check_lamp(self):
        if self._lamp is None:
            self.connect()

    def is_on(self) -> bool:
        self._check_lamp()
        return self._lamp.status().is_on

    def switch(self) -> None:
        self._check_lamp()
        self._lamp.off() if self.is_on() else self._lamp.on()

    def set_color(self, color: Union[str, tuple]) -> None:
        self._check_lamp()
        self._lamp.set_rgb(convert_color(color) if isinstance(color, str) else color)

    def set_brightness(self, brightness: int) -> None:
        self._check_lamp()
        self._lamp.set_brightness(brightness)


def convert_color(color: str) -> tuple:
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))


if __name__ == '__main__':
    s = SmartLamp(SmartLampSettings(ip='192.168.1.7', token='3d30dda82fac2d2d8e7d4cfc62315070',
                                    model='yeelink.light.color.5'))
    # s.switch()
    s.set_color('ff00ff')
