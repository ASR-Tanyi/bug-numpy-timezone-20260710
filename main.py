import ctypes
import numpy

lib = ctypes.CDLL('./build/libin.so')
result = ctypes.c_int()
lib.c_int_in(b"123", ctypes.pointer(result))
print(f"Result of c_int_in: {result.value}")
