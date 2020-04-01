#!/bin/bash

ls -l
echo -n "Number of simple files : "
ls -l | egrep '^-' | wc -l 
echo -n "Number of directories : "
ls -l | egrep '^d' | wc -l
echo -n "Number of hidden files : "
ls -ld .* | egrep '^-' | wc -l
echo -n "Number of hidden directories : "
ls -ld .* | egrep '^d' | wc -l
echo " End"
