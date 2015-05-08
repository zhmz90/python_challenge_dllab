#!/usr/bin/env python

s="One small letter surrounded by EXACTLY three big bodyguards on each of its sides"

words = s.split()

print words

for w in words:
    if len(w) == 4:
        print w
