#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys
import re

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        true = 0
        for i in word:
            if bool(re.search('[a-zA-Z]',i)) == True:
                true += 1
        if true == len(word):
            print('%s\t%s' % (word,1))
