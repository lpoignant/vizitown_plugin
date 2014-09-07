#!/bin/sh

files="vectors/*.py"
files+=" core/*.py"
files+=" ./*.py"

param="--max-line-length=160 --ignore=E265 "

./clear.sh

if has pep8-python2 2>/dev/null; then

	pep8-python2 $param $files

else

	pep8 $param $files

fi