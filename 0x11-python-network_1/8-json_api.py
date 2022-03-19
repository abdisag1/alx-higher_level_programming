#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        req_dic = req.json()
        id = req_dic.get('id')
        name = req_dic.get('name')
        if len(r_dic) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(req.dic.get('id'),req.dic.get('name')))
    except:
        print("Not a valid JSON")
