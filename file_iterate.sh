#!/bin/bash

second_file="/root/laxman.sh/first_file"
for first_file in $(cat $second_file)
do
	echo $first_file
done


