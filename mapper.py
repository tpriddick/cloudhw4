#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

lets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        word = word.lower()
        true = 0
        for i in word:
            if i in lets:
                true += 1
        if true == len(word):
            print('%s\t%s' % (word,1))
        else:
            print('%s\t$s' % (None,None))
