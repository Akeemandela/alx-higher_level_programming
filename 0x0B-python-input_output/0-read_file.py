#!/usr/bin/python3
"""defining read_file function in python"""

def read_file(filename=""):
    """reads filename using the utf-8 encoding"""
    with open(filename, r, encoding='utf-8') as f:
        print(f.read(), end="")
