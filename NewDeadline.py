import os
import datetime
import requests
import re
import json
import sys

try:
	port=sys.argv[1]
except:
	print "Too few arguments (Provide port)"
	exit()

# course=raw_input("Enter course code") 
link=raw_input("Enter clone URL (HTTPS/SSH) of deadline-repository\n")
#Extracting name of repo from link :
reponame=link.split('/')[-1].split('.git')[0] 
path=os.path.abspath(os.getcwd())

while True:
	time=raw_input("Enter deadline for submission (DD MM YYYY HH MM)\n")
	time=time.split(' ')
	try:
		timex=datetime.datetime(int(time[2]),int(time[1]),int(time[0]),int(time[3]),int(time[4]))
		assert(timex>datetime.datetime.now())
		break
	except: 
		print "Invalid date"

print("> Deadline  Details :\n")
print("  Deadline name : "+reponame)
print("  Deadline for submission : "+str(timex))
choice=raw_input("> Confirm deadline? (y/n) ")
if(choice=='y' or choice=='Y'):
	#Read from file of users
	try:
		f=open('students','r')
	except:
		print "File of students' list not found"
		exit()
	for line in f:
		line=line.rstrip('\n')
		userid=line.split(' ')[1]
		#Add compression script using 'at' command : http://www.computerhope.com/unix/uat.htm
		params={"clone_addr":link,"uid":userid,"repo_name":reponame,"private":"true"}
		r=requests.post("http://localhost:"+port+"/api/v1/repos/migrate", data = params)
	print("Deadline created!")
else:
  print("Deadline not created")	