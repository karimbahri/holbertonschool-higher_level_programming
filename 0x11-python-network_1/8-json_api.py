#!/usr/bin/python3
"""json request"""
if __name__ == '__main__':
    from sys import argv
    import requests
    try:
        link = argv[1]
    except:
        link = ""

    d = {'q': link}
    req = requests.post("http://0.0.0.0:5000/search_user", d)

    try:
        print("[{}] {}".format(req.json()['id'], req.json()['name']))
    except ValueError:
        print("Not a valid JSON")
    except:
        print("No result")
