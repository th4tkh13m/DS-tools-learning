"""
Main module that comparing speed between C and Python operation on array.
"""
import os
from time import time

if __name__ == "__main__":
    py_start = time()
    os.system("python python.py")
    py_time = time() - py_start

    c_start = time()
    os.system("./a.out")
    c_time = time() - c_start

    numpy_start = time()
    os.system("python numpy_arr.py")
    numpy_time = time() - numpy_start

    print(f"Python: {py_time}")
    print(f"C: {c_time}")
    print(f"Numpy: {numpy_time}")

    print(f"Relative: C is {py_time/c_time:2f} faster than python")
    print(f"Relative: Numpy is {py_time/numpy_time:2f} faster than python")
    print(f"Relative: C is {numpy_time/c_time:2f} faster than numpy")