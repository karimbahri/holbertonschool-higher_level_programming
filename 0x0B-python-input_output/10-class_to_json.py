#!/usr/bin/python3
"""10-class_to_json:
        functions:
            def class_to_json(obj):
"""


def class_to_json(obj):
    """"return dict repr of obj"""
    return obj.__dict__
