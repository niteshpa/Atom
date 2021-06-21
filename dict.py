#!/usr/bin/env python

def histogram(s):
    d = dict()
    for char in s:
        if char not in d:
            d[char]=1
        else:
            d[char]+=1
    return d

x=histogram("banalajdjdFHFGFJGF'ajgH")
print(x)
