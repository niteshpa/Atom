#!/usr/bin/env python
def factorial(n):
    if n==0:
        return 1
    else:
        var=n*factorial(n-1)
        return var

n=int(input("Enter the integer whose factorial is to be calculated: \n"))
print(factorial(n))
