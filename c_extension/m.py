import ctypes
from ctypes import *


def methodemo():
    lib = ctypes.CDLL("./c_f.so")
    m = lib.arithmetic
    m.argtypes = [c_char, c_double, c_double]
    m.restype = c_double
    print(m(c_char("+"), 123, 789))
    print(m(c_char("-"), 123, 789))
    print(m(c_char("*"), 123, 789))


if __name__ == "__main__":
    methodemo()
