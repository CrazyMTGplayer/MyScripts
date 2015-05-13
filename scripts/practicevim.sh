#!/bin/bash
#practicevim.sh will create a practice file from a template file
#appends new files name to header, then opens it in vim

echo "Creating new .py file from $1 to $2"
cp $1 $2
sed -i "1i#$2\n" $2
vim $2
