#!/usr/bin/python3
"""display url status"""
if __name__ == '__main__':
    from urllib import request
    r = request.Request("https://intranet.hbtn.io/status")
    with request.urlopen(r) as res:
        page = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode('utf-8')))
