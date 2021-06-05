#!/usr/bin/env python

s1 = int(input("Enter 1st Integer:\n"))
s2 = int(input("Enter 2nd Integer:\n"))
s3 = int(input("Enter 3rd Integer:\n"))
#print(s1,s2,s3)
#print(s1+s2)
if((s1 + s2) > s3) and ((s1 + s3) > s2) and ((s3 + s2) > s1):
    print("\nIts gonna form a Triangle /\\")
else:
    print("\nIts not gonna form a Triangle")
