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
    print(m(c_char("/"), 123, 789)) 


def test_pass_array(list_val):
    lib = ctypes.CDLL("./c_f.so")
    size = len(list_val)
    array_obj = c_int * size
    array = array_obj(*list_val)
    sum_array = lib.sum_array
    sum_array.argtypes = [array_obj, c_int]
    sum_array.restype = c_int
    return sum_array(array, size)


if __name__ == "__main__":
    methodemo()
