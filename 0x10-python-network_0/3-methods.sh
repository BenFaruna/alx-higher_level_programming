#!/bin/bash
# script that displays all allowed methods
curl -sI "$1" | grep Allow | cut -d " " -f2-
