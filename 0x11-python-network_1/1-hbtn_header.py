#!/usr/bin/python3
"""send request to url"""
if __name__ == "__main__":
    from sys import argv
    from urllib import request
    if len(argv) != 1:
        r = request.Request(argv[1])
        with request.urlopen(r) as page:
            print(page.info()["X-Request-Id"])
