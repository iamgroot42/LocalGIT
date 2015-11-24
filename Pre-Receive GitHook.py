#!/usr/bin/env python

import sys
import fileinput
import datetime

# Reject push if deadline expired
g=open('~/gogs-repositories/deadline','r')
now=datetime.datetime.now()
x=g.readline()
#Read deadline for this assignment from file
if(x<g) print"\nDeadline Passed\n"
#Abort the push if deadline passed
  sys.exit(1)

# Read in each ref that the user is trying to update
for line in fileinput.input():
#   print "POTATO says : You're a goat,Harry :) :) %s" % line
	print "\nPotato pushed ^_^\n"
# Abort the push
# sys.exit(1)