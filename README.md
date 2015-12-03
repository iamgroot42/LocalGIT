# SA-Project
Systems Administration project 

### Setup :
* Download and compile the latest version of <a href="https://github.com/gogits/gogs"> Gogs </a>
* Place the contents of this folder in the folder containing all the repositories
* Place your username and password in the 'config' file
* Place the list of usernames in the 'names' file (usernames)
* Run ``` python convertStudentList.py ``` to convert the 'names' list of users into a system-compatible file
* Run ```./gogs web``` for one-time setup
* Create new deadlines by running ```python NewDeadline.py <port>``` , where port is the port on which the Gogs server is being run (usualy 3000)
* Sit back and relax : any push requests after the deadline expires will be rejected.

Special thanks to <a href="https://github.com/Unknwon"> Unknwon </a> for modifying Gogs to support admin migration for all users and support for more githooks. 