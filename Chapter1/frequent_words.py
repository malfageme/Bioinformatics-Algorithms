#!/usr/bin/python

import sys

aStr = "GATATATGCATATACTT"
aPattern = "ATAT"

###############################################
# Read input from file or from Command Line
###############################################
if len(sys.argv) >= 2:
    if  sys.argv[1] == '-f':
        f = open (sys.argv[2], 'rU')
        f=f.readlines()
        aStr = f[0].strip()
        k = int(f[1])
    else:
        aStr = sys.argv[1]
        k = int(sys.argv[2])
else:
    print "Usage:", sys.argv[0]," -f <file> | String k"
    print ""
    exit()


################################
# Create the kmers dictionary
################################
myDict = {}
for i in range(0, len(aStr) - k):
    pattern = aStr[i:i+k]
    if pattern in myDict:
        myDict[pattern] += 1
    else:
        myDict[pattern] = 1


################################
# Print only the most frequent
################################
max = 0
for i in sorted(myDict, key=myDict.get, reverse=True):
    if myDict[i] < max:
        break
    else:
        max = myDict[i]
        print i,

