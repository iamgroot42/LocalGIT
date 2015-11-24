import os
import datetime
# Extract course code from current folder
# course=raw_input("Enter course code") 
name=raw_input("Enter name of deadline\n")
# print(os.getcwd())	
name=name.replace(" ","-") #Repo names can't have spaces
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
print("Deadline for submission : "+str(timex))
print("Deadline description :")
print(fd+"\n")
choice=raw_input("> Confirm deadline? (y/n)\n")
if(choice=='y' or choice=='Y'):
	# Add entry to file of deadlines,crontab
	print("Deadline created!")
else:
  print("Deadline not created")	