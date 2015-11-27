import os
import datetime
import requests
import re
import json
# Extract course code from current folder
# course=raw_input("Enter course code") 
link=raw_input("Enter HTTP URL of deadline-repository\n")
# Parse link to extract name of repo

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
print("  Deadline name : "+name)
print("  Deadline for submission : "+str(timex))
print("  Deadline description : ",fd)
choice=raw_input("> Confirm deadline? (y/n)\n")
if(choice=='y' or choice=='Y'):
	#Read from file of users	
	#Create repository <name> for each user in the list by the name 
	#Add pre-push hooks to each initialized repo
	#Add compression script using at command : http://www.computerhope.com/unix/uat.htm
	# For each user : 
	params={"clone_addr":link,"uid":userid,"repo_name":reponame,"private":"true"}
	r=requests.post("http://localhost:3000/api/v1/repos/migrate", data = params)
	assert(r.status_code==201)
	print("Deadline created!")
else:
  print("Deadline not created")	