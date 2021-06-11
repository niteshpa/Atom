#!/usr/bin/env python
count=0
file = open("crosswords.txt")
for line in file:
    word=line.strip()
    if "e" not in word:
        print(word)
        count=count+1

print("\nTotal: ", count)
