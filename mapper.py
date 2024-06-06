import sys 

letters = set('abcdefghijklmnopqrstuvwxyz')
  
for line in sys.stdin: 
    line = line.strip() 
    words = line.split() 
    for word in words:
        word = word.lower()
        if word[0] in letter:
            print('%s\t%s' % (word, 1))
