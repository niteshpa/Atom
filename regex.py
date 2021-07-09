#!/usr/bin/env python
#uses of findall 
import re
x="I am in cloud 9 87 654 3210"
y=re.findall("[0-9]+", x)
print(y) #it's gonna extract all the matches from the line x

#greedy findall() + & * char
x= "I am the: boss:"
y=re.findall("^I.+:", x)
print(y)

#making it non-greedy using '?' char

x= "I am the: boss:"
y=re.findall("^I.+?:", x)
print(y)

#output
#['9', '87', '654', '3210']
#['I am the: boss:']
#['I am the:']
