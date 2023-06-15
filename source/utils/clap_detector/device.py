#!/usr/bin/python3
import os
import sys

import pyaudio

from smart_home.source.utils.clap_detector.config import Config


class Device:
    def __init__(self, config: Config):
        self._stream = None
        self._config = config
        self._input = pyaudio.PyAudio()

        os.system('clear')
        self._set_input_device()

    def open_stream(self):
        if self._stream is None:
            self._stream = self._input.open(
                format=pyaudio.paInt16,
                channels=self._config.channels,
                rate=self._config.rate,
                input=True,
                frames_per_buffer=self._config.chunk_size
            )

    def read_data(self):
        return self._stream.read(self._config.chunk_size)

    def close_stream(self):
        self._stream.stop_stream()
        self._stream.close()

    def _set_input_device(self):
        if self._input.get_host_api_count() < 1:
            print("No supported PortAudio Host APIs are found in your system")
            sys.exit(1)

        if self._input.get_device_count() < 1:
            print("No input audio device is found in your system")
            sys.exit(1)

        self.defaultDevice = self._input.get_default_input_device_info()
        self._config.channels = int(self.defaultDevice['maxInputChannels'])
        self._config.rate = int(self.defaultDevice['defaultSampleRate'])

    def __del__(self):
        self._input.terminate()
