import ctypes
import numpy

timezone_lib = ctypes.CDLL('./build/libtimezone.so')
timezone = b"America/New_York"
original = 1697040000
timestamp = ctypes.c_int64(original)
timezone_lib.c_to_local(ctypes.c_char_p(timezone), ctypes.pointer(timestamp))
print(f"UTC time {original} is local time {timestamp.value} in {timezone.decode()}")
