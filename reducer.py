from operator import itemgetter
import sys
import re

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t',1)
    try:
        count = int(count)
    except ValueError:
        continue
    true = 0
    for i in word:
        if bool(re.search('[a-zA-Z]',i)) == True:
            true += 1
    if len(word) == true:
        if current_word == word:
            current_count += count
        else:
            if current_word:
                print('%s\t%s' % (current_word, current_count))
            current_count = count
            current_word = word
if current_word == word:
    print('%s\t%s' % (current_word, current_count))
