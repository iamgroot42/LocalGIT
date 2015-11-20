# Extract course code from current folder
# course=raw_input("Enter course code") 
name=raw_input("Enter name of deadline")
name=name.replace(" ","-") #Repo names can't have spaces
while True:
	time=raw_input("Enter deadline for submission (DD MM YYYY HH MM)")
	time=time.split(' ')
	try:
		time=datetime.datetime(int(time[2]),int(time[1]),int(time[0]),int(time[3]),59)
		break
	except: 
		print "Invalid format!"
fd=raw_input("Enter name of file containing description")
