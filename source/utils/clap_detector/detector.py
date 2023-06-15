#!/usr/bin/python3
import _thread as thread
from array import array
from time import sleep
from typing import Callable

from smart_home.source.utils.clap_detector.device import Device
from smart_home.source.utils.clap_detector.config import Config


class Detector:
    def __init__(self, config: Config | None = None):
        self._config = config or Config()
        self.claps = 0
        self.lock = thread.allocate_lock()
        self.device = Device(self._config)

    def start(self, callback: Callable) -> None:
        try:
            self.device.open_stream()
            print("Clap detection started")
            while not self._config.exit:
                try:
                    data = self.device.read_data()
                except (OSError, IOError):
                    data = None

                if self._find_clap(data):
                    self.claps += 1

                if self.claps == 1 and not self.lock.locked():
                    thread.start_new_thread(self._listen_claps, (callback,))

        except(KeyboardInterrupt, SystemExit):
            pass
        self.stop()

    def _expect_clap(self, clap: int) -> None:
        sleep(self._config.wait)
        if self.claps > clap:
            self._expect_clap(self.claps)

    def _listen_claps(self, callback: Callable):
        with self.lock:
            print("Waiting for claps...")
            self._expect_clap(self.claps)

            if self.claps == self._config.clap_count:
                callback()

            print("You clapped", self.claps, "times.")
            self.claps = 0

    def stop(self):
        print("Exiting")

        self.device.close_stream()
        del self.device

    def _find_clap(self, data: bytearray | None) -> bool:
        byte_stream = array('b', [0]) if data is None else data
        max_value = max(array('h', byte_stream))
        if max_value > 15000:
            print(f"Clap detected on {max_value}")
        return max_value > self._config.clap_algorithm_value
