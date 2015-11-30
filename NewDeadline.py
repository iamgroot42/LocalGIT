import os
import datetime
import requests
import re
import json
import sys
import urllib 
import getpass

try:
	f=open('config','r')
	username=f.readline().rstrip()
	username=username.split(':')[1]
	password=f.readline().rstrip()
	password=password.split(':')[1]
	f.close()
except:
	print "Configuration file not found"
	exit()

try:
	port=sys.argv[1]
except:
	print "Too few arguments (Provide port)"
	exit()

# Prepare session
s = requests.Session()
r=s.get("http://localhost:3000/user/login");
i_like_gogits=urllib.unquote(r.cookies['i_like_gogits']).decode('utf8')
lang=urllib.unquote(r.cookies['lang']).decode('utf8')
csrf=urllib.unquote(r.cookies['_csrf']).decode('utf8')
dicto={"user_name":username, "password":password ,"_csrf":csrf}
r2=s.post("http://localhost:3000/user/login",data=dicto)

link=raw_input("Enter clone URL (HTTPS/SSH) of deadline-repository\n")
#Extracting name of repo from link :
reponame=link.split(os.sep)[-1].split('.git')[0] 
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
		name,userid=line.split(' ')
		dest_path=name+os.sep+reponame+".git"+os.sep+"hooks"+os.sep+"pre-receive"
		source_path="githook"
		#Copy githook :
		print "SOURCE "+source_path
		print "DEST "+dest_path
		params={"clone_addr":link,"uid":userid,"repo_name":reponame,"private":"true"}
		print "http://localhost:"+port+"/api/v1/repos/migrate"
		r3=s.post("http://localhost:"+port+"/api/v1/repos/migrate", data = params)
		try:
			assert(r3.status_code/100==2) #2xx return code <-> Success
		except:
			print "Error initializing data into users' repositories"
			exit()
		os.system("cp "+source_path+" "+dest_path)
		os.system("chmod +x "+dest_path)
	f=open(reponame+'_deadline','w')
	f.write(timex.strftime("%Y-%m-%d %H:%M"))
	f.close()
	print("Deadline job created!")
	# Change this to deadline time + 5 minutes :
	at_time="at "+time[3]+":"+time[4]+" "+time[1]+"/"+time[0]+"/"+time[2]
	# Fix error with folowing line 
	automation="bash prepare.sh"+" | "+at_time
	os.system(automation)
else:
  print("Deadline not created")	
