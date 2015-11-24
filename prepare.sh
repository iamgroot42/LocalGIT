#!/bin/bash
#works with command line arguments
#./sascript.sh /home/mansi/github 2
SHELL=/bin/sh
DIR=$1/*/
n=$2
count=0
check=1
DIRZ=~/Desktop/zipped
echo "n is $2"
echo "directory is $1"
mkdir $DIRZ
mkdir $DIRZ/1
FILE=$check.tar.gz.
for f in $DIR
do
	echo "directory is $f"
	if [ $count -lt $n ]; 
	then
		cp -avr $f $DIRZ/$check
		count=$((count+1))
	else	 
		count=0
		check=$((check+1))
		mkdir $DIRZ/$check
		cp -avr $f $DIRZ/$check
		count=$((count+1))
	fi
	
done
count=1
for f in $DIRZ/*/
do
		tar -cvzf $DIRZ/$count.tar $f
		count=$((count+1))
		echo "compressed" 
done


for f in $DIRZ/*/
do
		rm -rf $f
		echo "deleted" 
done

