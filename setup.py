import setuptools

PACKAGE_NAME = 'smart_home'
VERSION = '1.0'
AUTHOR = 'Betal Berbekov'

DEPS = [
    'fastapi',
    'pyaudio',
    'pydantic',
    'python-miio',
    'uvicorn',
    'ioc',
]


def setup():
    setuptools.setup(
        name=PACKAGE_NAME,
        version=VERSION,
        author=AUTHOR,
        description='smart_home',
        packages=[PACKAGE_NAME],
        package_dir={PACKAGE_NAME: 'source'},
        include_package_data=True,
        package_data={'': ['*/*', '*/**/*', '*/**/**/*']},
        install_requires=DEPS
    )


if __name__ == "__main__":
    setup()
