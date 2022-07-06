#!/usr/bin/python3
"""module for bringing arguments together"""
import sys
import os

save_json_file = __import__("5-save_to_json_file").save_to_json_file
load_json_file = __import__("6-load_from_json_file").load_from_json_file

file = "add_item.json"
json_list = []
if os.path.exists(file):
    json_list = load_json_file(file)

for elem in range(1, len(sys.argv)):
    json_list.append(sys.argv[elem])

save_json_file(json_list, file)
