#!/usr/bin/python3
"""8-load_from_json_file"""
import json


def load_from_json_file(filename):
    """load object from file"""
    with open(filename, "r") as my_file:
        return json.loads(my_file.read())
