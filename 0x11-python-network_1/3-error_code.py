#!/usr/bin/python3
"""display the body of webpage"""
if __name__ == "__main__":
    from sys import argv
    from urllib import request
    try:
        r = request.Request(argv[1])
        with request.urlopen(r) as res:
            res = ress.read()
            print(res.decode('utf-8')
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
