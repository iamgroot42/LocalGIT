# SA-Project
Systems Administration project 

### Setup :
* gitlab-ctl start
* ```./gogs web``` for one-time setup ( Database type : SQLite3, run user : current user)

### Tentative features 

* Setting up docker.
* Setting up Gogs.
* Script to back up repositories every now ant then (defined by user).
* Server side git-hook to reject push requests after deadline expires.
* Server side hook to reject push requests if format of files is changed.
* Script to zip compress repositories and send compressed sets of assignments to teaching assistants randomly via email (saving the hassle of TAs opening database and manually downloading assignments to check).

## Reasons for using a local git server :

* Submissions are mostly made from the college's network.
* Students first create repositories on GitHub (wasting private repo), then submit via backpack.Wastes bandwidth (while working on GitHub ; too less net used but nonetheless) and private repositories.
* Out of the students ending up with plagiarism charges,we want to make sure that none of them actually plagiarised (want to minimize false positives as much as we can : making it 0 in the ideal case).
* In such cases,using a local git server provides felxibility to the TAs,instructors as well as students.
* Students don't have to waste private repoitories to work on assignments.
* If a student fails to complete an assignment, they can be awarded partial marks (as their work exist in the repository).Students don't have to upload assignments after completing them.Hence,no cases of 'forgetting to upload' or 'deadline extensions because of time taken to compress submission'.
* Instructor is the admin : controls all the push requests.Can enforce structural conditions on submissions to make it easier to check them.Can ignore push requests after deadline expires.
* This along with scripts, makes it easier to compile assignments for checking to be done by the TAs.The system can be automated to compress submissions into groups and automatically mailing to the TAs , hence saving time spent by TAs in downloading submissions individually and then checking them (uncompressing them as well :p ).

## Reasons for chosing Gogs over other local git servers 

* Written in 'Go' language (developed by Google ; highly optimized,scalable).
* Support for dockers (just one package,run with just a single command).
* Support for dockers.
* Negligible resource usage (minimum 8MB RAM and one core CPU required).
