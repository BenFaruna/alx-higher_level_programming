#!/usr/bin/python3
"""module to get the header X-Request-Id"""
import requests

if __name__ == '__main__':
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print(r.headers['X-Request-Id'])
