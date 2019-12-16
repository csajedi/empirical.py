""" This is a one-to-one translation of the 1D and 2D simulation software in C++ provided at : https://www.algorithmicdynamics.net/software.html """

from enum import Enum

class direction(Enum):
    LEFT=1
    RIGHT=2
    STOP=3