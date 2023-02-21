#!/bin/bash

echo press any options below
echo press 1 to show present working directory
echo press 2 list files in current directory
echo press 3 to display the date

read choice

case $choice in
	1)pwd;;
	2)ls -ltr;;
	3)date;;
	*)echo Invalid Options
esac
