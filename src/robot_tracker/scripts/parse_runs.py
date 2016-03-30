#!/usr/bin/env python

"""
Author: Brandon Kallaher (brandon.kallaher@wsu.edu)
Description:
    Uses parse_run.py to parse a full directory of runs
"""

from parse_run import parse_run
from os import walk
from fnmatch import filter as ffilter

# for root, dir, files in walk("/home/bkallaher/runs"):
#     print root
#     print ""
#     print dir
#     for item in ffilter(files, "*.csv"):
#         print "\t" + item
#     print ""


for root, dirs, files in walk("/home/bkallaher/runs"):
    for dir in dirs:
        for root, dirs, files in walk("/home/bkallaher/runs/" + dir):
            print root
            for item in ffilter(files, "*.csv"):
                print parse_run(root + '/', item, "/home/bkallaher/runs/base.csv")
        print ""
