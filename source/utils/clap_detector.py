from smart_home.source.utils.clap_detector import Detector


def call_smart_lamp():
    # smart_lamp = SmartLamp(SmartLampSettings(ip='192.168.1.7', token='3d30dda82fac2d2d8e7d4cfc62315070'))
    # smart_lamp.switch()
    print('clapp')


def main():
    listener = Detector()
    listener.start(call_smart_lamp)


if __name__ == '__main__':
    main()
