#!/usr/bin/python3
"""module to get error codes of pages"""
import sys
import requests

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    if r.status_code == 200:
        print(r.text)
    else:
        print(r.status_code)
