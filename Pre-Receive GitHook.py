#!/usr/bin/env python
import os
import sys
import fileinput
import datetime

# Reject push if deadline expired
curdir=os.getcwd().split(os.sep)
rep_name=curdir[-2].split('.git')[0]
wanted_dir=curdir[:len(curdir)-3]
os.chdir(os.sep.join(wanted_dir))
rep_name+="_deadline"
f=open(rep_name,'r')
deadline=datetime.datetime.strptime(f.readline(),'%Y-%m-%d %H:%M')
f.close()
now=datetime.datetime.now()
#Read deadline for this assignment from file
if(now<deadline):
	print"\nDeadline Passed\n"
	sys.exit(1)

# Read in each ref that the user is trying to update
for line in fileinput.input():
	print "\nPotato pushed ^_^\n"