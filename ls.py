#! /usr/bin/env python

"""
Print list of files.

By default take curent working directory.
"""
__version__ = "0.0.1"
__author__ = "luka.marinko@gmail.com"

import os
import os.path
import sys

import argparse

util="ls"
_shortdesc = "list files"

def version(author, version, name, description):
    out="Marinko's utils. Command [{}] v{}.\nBy {}".format(name, version, author)
    print(out)

def command_ls(opts):
    d= os.getcwd()
    files=os.listdir(d)
    for f in files:
        print(f)

def output(files, opts):
    cnt = len(files)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.parse_args()

    opts = {}
    command_ls(opts)
