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
    output_cols(files, opts)

def output(files, opts):
    cnt = len(files)

def output_cols(files, opts, spacing=1):
    colwidth = max(len(w) for w in files) + spacing
    cols = opts.cols // colwidth
    rows = list_to_columns(files, cols)

    for row in rows:
        line = "".join(item.ljust(colwidth) for item in row)
        print(line)
        
def list_to_columns(ls, cols):
    """
    Split flat list into list of [cols] colums

    example:
        try:
        l = [1, 2, 3, 4, 5]
        ret = list_to_columns(ls, 2)
        ret 
        [[1, 3], [2, 4], [5]]
    """
    rows = len(ls) //int(cols)
    if len(ls) % cols:
        rows += 1
    ret = []
    for i in range(rows):
        ret.append(ls[i::rows])
    return ret

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
