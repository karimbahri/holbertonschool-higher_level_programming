#!/usr/bin/python3
"""6-from_jason_string"""
import json


def from_json_string(my_str):
    """from_json_string: string to obj"""
    obj_json = json.loads(my_str)
    return obj_json
