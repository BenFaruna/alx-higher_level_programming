#!/bin/bash
# script that sends data via post request
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
