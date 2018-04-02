#!/usr/bin/env python
import sys
 
# maps words to their counts
word2count = {}
 
# input comes from STDIN
for line in sys.stdin:
   
     # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count
rank = 1
for key, value in sorted(word2count.iteritems(), key=lambda (k,v): (v,k),reverse=True):
	print '%s\t%s'% (key,"Total Value: "+ str(value) + " Rank: "+ str(rank))
	rank = rank +1

