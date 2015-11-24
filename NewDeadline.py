import os
import datetime
import re
# Extract course code from current folder
# course=raw_input("Enter course code") 
name=raw_input("Enter name of deadline\n")
replaced=re.sub('[^A-Za-z0-9_.-]','-',name) #Regex for permitted repo names
# print(os.getcwd())	
while True:
	time=raw_input("Enter deadline for submission (DD MM YYYY HH MM)\n")
	time=time.split(' ')
	try:
		timex=datetime.datetime(int(time[2]),int(time[1]),int(time[0]),int(time[3]),int(time[4]))
		assert(timex>datetime.datetime.now())
		break
	except: 
		print "Invalid date"

fd=raw_input("Enter description for deadline \n")
print("> Deadline  Details :\n")
print("Deadline name : "+replaced)
print("Deadline for submission : "+str(timex))
print("Deadline description : ",fd)
choice=raw_input("> Confirm deadline? (y/n)\n")
if(choice=='y' or choice=='Y'):
	#Read from file of users	
	#Create repository <name> for each user in the list by the name 
	#Add pre-push hooks to each initialized repo
	#Add compression script to crotab 
	print("Deadline created!")
else:
  print("Deadline not created")	