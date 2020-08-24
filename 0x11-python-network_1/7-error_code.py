#!/usr/bin/python3
"""post request and print body"""
if __name__ == "__main__":
    from sys import argv
    import requests
    req = requests.get(argv[1])
    status = req.status_code
    body = req.text
    if status >= 400:
        print("Error code:", status)
    else:
        print(body)
