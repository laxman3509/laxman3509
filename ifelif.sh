#! /bin/bash

word=a
if [ $word = "b" ]
then
	echo "condition is false"
elif [ $word = "a" ]
then
	echo "condition is true"
else
	echo "condition is not avalible"
fi

