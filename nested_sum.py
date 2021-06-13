#!/usr/bin/env python

sum = 0

t=[[1,2,3],[4,5,6],[7,8,9,10],[11],[12]]

for x in t:
    for i in x:
        sum+=i
print("Total: ", sum)
