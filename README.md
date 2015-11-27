# SA-Project
Systems Administration project 

### Setup :
* gitlab-ctl start
* ```./gogs web``` for one-time setup ( Database type : SQLite3, run user : current user)

### Tentative features 

* [?]Setting up docker.
* Setting up Gogs.
* [done]Server side git-hook to reject push requests after deadline expires.
* [done]Script to zip compress repositories and make compressed sets of assignments.

## Reasons for using a local git server :

* Submissions are mostly made from the college's network.
* Students first create repositories on GitHub (wasting private repo), then submit via backpack.Wastes bandwidth (while working on GitHub ; negligible net used but nonetheless) and private repositories.
* Out of the students ending up with plagiarism charges,we want to make sure that none of them actually plagiarised (want to minimize false positives as much as we can : making it 0 in the ideal case) by tracking commits (without being a contributor for any of them).
* In such cases,using a local git server provides felxibility to the TAs,instructors as well as students.
* Students don't have to waste private repoitories to work on assignments.
* If a student fails to complete an assignment, they can be awarded partial marks (as their work exist in the repository).Students don't have to upload assignments after completing them.Hence,no cases of 'forgetting to upload' or 'deadline extensions because of time taken to compress submission'.
* Instructor is the admin : controls all the push requests.Can enforce structural conditions on submissions to make it easier to check them.Can ignore push requests after deadline expires.
* This along with scripts, makes it easier to compile assignments for checking to be done by the TAs.The system can be automated to compress submissions into groups and automatically mailing to the TAs , hence saving time spent by TAs in downloading submissions individually and then checking them (uncompressing them as well :p ).

## Reasons for chosing Gogs over other local git servers 

* Written in 'Go' language (developed by Google ; highly optimized,scalable).
* Support for dockers (just one package,run with just a single command).
* Negligible resource usage (minimum 8MB RAM and one core CPU required).

##Setting it up

* Download the repo from https://github.com/iamgroot42/gogs
* Navigate into the folder and run ```go build```
* Set up server ```./gogs web```
* Move the githook into the hooks folder of the repo and test it once.
* If successful, modify it to compare directory structure with predefined structure (to make submissions easier to check for TAs).

-> No need to modify gogs,master branch updated
-> API modified for adding repos as admin via CLI

@Unknwon rocks *_*

GET /repos/:username/:reponame/archive/:ref:format , ref=name of commit(opt), format=.tar.gz

TODO : 
* Check scripts on updated gogs
* Figure out why POST/GET requests don't work via CTL/Python
* Find a way to include githooks while migrating/ add them manually (stupid)
* UI tweaks
