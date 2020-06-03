#!/usr/bin/python3
"""7-save_to_jason_file"""
import json


def save_to_json_file(my_obj, filename):
    """save to jason file"""
    with open(filename, "w") as my_file:
        my_file.write(json.dumps(my_obj))
