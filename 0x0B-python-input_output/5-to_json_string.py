#!/usr/bin/python3
"""
5-to_json
    functions:
        to_json_string
"""
import json


def to_json_string(my_obj):
    """to_json_string: return jason repr of my_obj"""
    json_obj = json.dumps(my_obj)
    return json_obj
