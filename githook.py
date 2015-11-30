#!/usr/bin/env python
import os
import sys
import fileinput
import datetime

# Reject push if deadline expired
curdir=os.getcwd().split(os.sep)
# print curdir
rep_name=curdir[-1].split('.git')[0]
# print rep_name
wanted_dir=curdir[:len(curdir)-2]
# print wanted_dir
os.chdir(os.sep.join(wanted_dir))
# print os.getcwd()
rep_name+="_deadline"
# print rep_name
f=open(rep_name,'r')
deadline=datetime.datetime.strptime(f.readline(),'%Y-%m-%d %H:%M')
f.close()
now=datetime.datetime.now()
#Read deadline for this assignment from file
if(now<deadline):
	print"\nDeadline Passed!\n"
	sys.exit(1)

# Read in each ref that the user is trying to update
for line in fileinput.input():
	print "\nPush successful!\n"
