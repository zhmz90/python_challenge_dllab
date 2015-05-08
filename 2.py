#!/usr/bin/env python


riddle = []
ret = ""
with open("ocr.txt") as f:
    for line in f:
        for c in line:
            if c in ["e","q",""]:
                ret+=c;
            if c not in riddle:
                riddle.append(c)
print riddle

