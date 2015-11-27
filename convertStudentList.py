import sys
import requests

try:
	fname=sys.argv[1]
	port=sys.argv[2]
except:
	print "Too few arguments (Provide input filename,port)"
	exit()

f=open(fname,'r')
g=open('output','w')

for line in f:
	line=line.rstrip('\n')
	link="http://localhost:"+str(port)+"/api/v1/users/"+line
	r=requests.get(link)
	try:
		idee=r.json()['id']
		g.write(line+" "+str(idee)+"\n")
	except:
		print "Error. (Might be because of username : "+line+")"
		break

print "Output file generated!"
