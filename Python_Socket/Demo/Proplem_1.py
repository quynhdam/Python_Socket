from typing import Any, Union
from math import *
import os

def Main():
    print("Nhap vao so n:")
    x = int(input())
    print("kieu cua x la: ", type(x))
    sum = 0
    print("kieu cua sum la: ", type(sum))
    x1 = x
    while x1 > 0:
        n = x1 % 10
        sum = sum + n
        x1 = x1 // 10
    print("Tong cac chu so cua", x, "la", sum)
Main()