#!/usr/bin/python3
"""9-add_item: add item to json file"""
from sys import argv
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

try:
    ls_object = load_from_json_file("add_item.json")
except:
    ls_object = []

ls_object += argv[1:]

save_to_json_file(ls_object, "add_item.json")
