# add the path of the submodule to the system's path
from sys import path as sys_path
from os import path
sys_path.append(path.dirname(path.abspath(__file__)))