#!/usr/bin/python3
# -*-coding:utf-8 -*

# Shamelessly taken from stackoverflow
# https://stackoverflow.com/questions/22520932/python-remove-all-non-alphabet-chars-from-string/22521156#22521156
import sys
import re


for line in sys.stdin:
    line = line.strip()
    words = line.split()
    good = re.compile('[^a-zA-Z]')
    for word in words:
        word = word.lower()
        word = good.sub('',word)
        print('%s\t%s' % (word,1))
