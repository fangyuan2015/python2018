#!/usr/bin/env python
#coding=utf-8

import re

it = re.finditer(r"\d+","12a32bc43jf3")
print it
for match in it:
    print (match.group())
