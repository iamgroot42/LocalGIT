#!/bin/bash
#works with command line arguments
#./sascript.sh /home/mansi/github 2
SHELL=/bin/sh
FILENAME=$1/potato.txt
FOLDER=$2
n=$3
count=1
check=1
DIRZ=~/Desktop/zipped
echo "n is $3"
echo "directory is $1"
declare -a var
mkdir $DIRZ
FILE=$check.tar.gz.
cat $FILENAME | while read LINE
do
	echo "directory is $LINE"
	if [ $count -le $n ]; 
	then
		#cp -avr $f $DIRZ/$check
		var[$count]=$LINE
		count=$((count+1))
	else	 
		count=1
		# mkdir $DIRZ/$check
		tar -cvzf $DIRZ/$check.tar $FILENAME/${var[*]}/$FOLDER
		echo "compressed"
		check=$((check+1))
		unset var
		declare -a var
		var[$count]=$LINE
		count=$((count+1))
	fi
# let count++
echo "$LINE"
done

if [ $count -gt 1]]
then
		tar -cvzf $DIRZ/$check.tar $FILENAME/${var[*]}/$FOLDER
		# count=$((count+1))
		echo "compressed" 
fi

echo "--------ALL DONE----------"
# for f in $DIRZ/*/
# do
# 		rm -rf $f
# 		echo "deleted" 
# done
