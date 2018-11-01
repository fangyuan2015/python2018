#!/usr/bin/env python
#coding=utf-8

import re

line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*',line,re.M|re.I)

if searchObj:
    print "searchObj.group():",searchObj.group()
    print "saerchObj.group(1):",searchObj.group(1)
    print "searchObj.group(2):",searchObj.group(2)
else:
    print "Nothing found!!"
