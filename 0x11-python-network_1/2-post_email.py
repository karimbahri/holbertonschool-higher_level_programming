#!/usr/bin/python3
"""send post request"""
if __name__ == '__main__':
    from sys import argv
    from urllib import request
    from urllib import parse
    link = argv[1]
    args = {'email': argv[2]}
    enc_d = parse.urlencode(args).encode("ascii")
    r = request.Request(link, enc_d)
    with request.urlopen(r) as res:
        page = res.read()
        print(page.decode("ascii"))
