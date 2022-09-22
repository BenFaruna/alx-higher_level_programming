#!/bin/bash
# script that displays the size of the body response

if [ $# -eq 1 ]
then
	curl -so /dev/null -w '%{size_download}\n' "$1"
fi

