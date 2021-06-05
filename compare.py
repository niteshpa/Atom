#!/usr/bin/env python

def compare(x,y):
    if (x>y):
        return 1
    elif(x==y):
        return 0
    else:
        return -1
x=int(input("Enter the first Number: \n"))
y=int(input("Enter the second Number: \n"))
print("---------------")
print(compare(x,y))
