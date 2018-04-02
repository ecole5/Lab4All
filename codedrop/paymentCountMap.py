#!/usr/bin/env python
import sys
 
#--- get all lines from stdin ---
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()

    #--- split the line into words ---
    words = line.split("\t")

    #--- output tuples [word, 1] in tab-delimited format---A
    for i in range(0, len(words)): #start at 1 for modulo count to work properly
    	if (i+1) % 6 == 0:
		print '%s\t%s' % (words[i], words[i-1])

