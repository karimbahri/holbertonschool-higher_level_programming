#!/usr/bin/python3
"""fetch url"""
if __name__ == "__main__":
    import requests
    print("Body response:")
    req = requests.get('https://intranet.hbtn.io/status')
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
