from setuptools import setup

DEPS = [
    'fastapi',
    'pyaudio',
    'pydantic',
    'python-miio',
]


setup(
    name='smart_home',
    version='1.0.0',
    packages=['utils', 'services', 'settings'],
    url='',
    license='',
    author='Betal Berbekov',
    author_email='',
    description=''
)
