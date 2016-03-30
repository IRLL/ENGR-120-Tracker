#!/usr/bin/env python

"""
Author: Brandon Kallaher (brandon.kallaher@wsu.edu)
Description:
    Uses parse_run.py to parse a full directory of runs
"""

from parse_run import parse_run
from os import walk
from fnmatch import filter as ffilter
from shutil import rmtree as rmdir #Need this function in order to delete tmp dir without deleting tmp files
import json

scores = {}

for root, dirs, files in walk("/home/bkallaher/runs"):
    for dir in dirs:
        for root, dirs, files in walk("/home/bkallaher/runs/" + dir):
            print root
            for item in ffilter(files, "*.csv"):
                scores[item[:-4] + "-" + root[-4:]] =  parse_run(root + '/', item, "/home/bkallaher/runs/base.csv")
            rmdir(root + "/tmp", ignore_errors=True)
        print ""

f = open("/home/bkallaher/runs/scores.json", 'w+')
json.dump(scores, f)
f.close()
