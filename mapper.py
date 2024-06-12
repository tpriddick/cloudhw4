#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys


for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        word = word.lower()
        if word.isalpha():
            print('%s\t%s' % (word,1))
        else:
            print('%s\t%s' % (word,0))
