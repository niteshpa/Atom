#!/usr/bin/env python
import re
fhand = open("regex_sum.txt")
total=0
for line in fhand:
    x=re.findall("[0-9]+", line)
    if len(x)== 0:
        continue
    else:
        x = [int(i) for i in x]
        total=total + sum(x)

print(total)
