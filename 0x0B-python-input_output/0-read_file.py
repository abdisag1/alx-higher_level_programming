#!/usr/bin/python3
"""
Contains the read file function
"""


def read_file(filename=""):
    """ opens the file to read text in UTF8"""
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data,end="")


