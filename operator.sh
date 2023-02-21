#! /bin/bash
##search for file##
#echo -e "Enter the name of the file: "
#read file_name

#if [ -e $file_name ]
#then
#	echo "$file_name file found"
#else
#	echo "$file_name file not found"
#fi


## search for directories ##

#echo -e "Enter the name of the directory: \c"
#read directory_name

#if [ -d $directory_name ]
#then
#	echo "$directory_name directory exits"
#else
#	echo "$directory_name directory not exits"
#fi

echo -e "Enter the name of the file: \c"
read file_name

if [ -w $filename ]
then
	echo "$file_name have permission"
else
	echo "$file_name not have permission"
fi

