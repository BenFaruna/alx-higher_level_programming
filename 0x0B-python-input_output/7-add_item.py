#!/usr/bin/python3
"""module for bringing arguments together"""
import sys
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """function that facilitates the writing of arguments into a JSON file"""
    args = []
    if not os.path.exists("add_item.json"):
        with open("add_item.json", "a"):
            save_to_json_file(list(), "add_item.json")

    args = load_from_json_file("add_item.json")
    if len(sys.argv) <= 1:
        return

    for arg in sys.argv[1:]:
        args.append(arg)
    save_to_json_file(args, "add_item.json")


if __name__ == "__main__":
    main()
