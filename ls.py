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
from termutil import term_size, isterminal

util="ls"
_shortdesc = "list files"

def version(author, version, name, description):
    out="Marinko's utils. Command [{}] v{}.\nBy {}".format(name, version, author)
    print(out)

def command_ls(opts):
    d= os.getcwd()
    files=os.listdir(d)

    # Filter files according to -a flag
    if not opts.all:
        files = [f for f in files if f[0] != "."]
    for f in files:
        print(f)

def output(files, opts):
    cnt = len(files)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--all", help="all files. Do not ignore entries starting with .", action="store_true" )
    opts = parser.parse_args()
    opts.terminal = isterminal(sys.stdout.fileno())
    if opts.terminal:
        r,c = term_size(sys.stdout.fileno())
        opts.rows = r
        opts.cols = c
    print("Rows: {}, Columns: {}".format(opts.rows, opts.cols)) 
    command_ls(opts)
