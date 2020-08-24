#!/usr/bin/python3
"""send request"""
if __name__ == '__main__':
    from sys import argv
    import requests
    link = argv[1]
    req = requests.get(link)
    print(req.headers["X-Request-Id"])
