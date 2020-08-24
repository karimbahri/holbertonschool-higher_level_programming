#!/usr/bin/python3
"""github id"""
if __name__ == "__main__":
    import requests
    from sys import argv
    link = "https://api.github.com/user"
    user = argv[1]
    access_token = argv[2]
    req = requests.get(link, auth=HTTPBasicAuth(user, access_token))
    try:
        print(req.json()['id'])
    except:
        print("None")
