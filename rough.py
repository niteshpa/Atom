#!/usr/bin/env python
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        counts[words[1]]=counts.get(words[1],0) + 1

maxword = None
maxcount = None

for word,count in counts.items():
    if maxcount is None or count>maxcount:
        maxword=word
        maxcount=count

print(maxword, maxcount)
