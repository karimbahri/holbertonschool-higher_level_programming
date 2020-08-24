#!/usr/bin/python3
"""send request and print the body"""
if __name__ == '__main__':
    import requests
    from sys import argv
    link = argv[1]
    data = {"email": argv[2]}
    req = requests.post(link, data)
    print(req.text)
