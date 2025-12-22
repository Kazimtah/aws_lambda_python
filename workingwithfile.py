from os import path 

print(path.abspath('.'))
print(type(path))

from pathlib import Path 

print(Path('.').absolute())

print(Path('usr').joinpath('local').joinpath('bin'))

print(Path('usr/local/bin'))

print(Path('main.py').exists())
print(Path('/kazim/home/Desktop').exists())
print(Path('other.py').exists())