#!/usr/bin/env python
#coding=utf-8

import re

s = '42112719850526'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
print (res.groupdict())

