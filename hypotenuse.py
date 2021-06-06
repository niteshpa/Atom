#!/usr/env/python
import math
def hypotenuse(l,b):
    h_sq=(l**2) + (b**2)
    return math.sqrt(h_sq)

print(hypotenuse(3,4))
