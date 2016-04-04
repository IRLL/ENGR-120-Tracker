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
from os import environ

scores = {}

for root, dirs, files in walk(environ('HOME') + "/runs"):
    for dir in dirs:
        for root, dirs, files in walk(environ('HOME') + "/runs/" + dir):
            print root
            for item in ffilter(files, "*.csv"):
                scores[item[4:-4] + "-" + root[-4:]] =  parse_run(root + '/', item, environ('HOME') + "/runs/base.csv")
            rmdir(root + "/tmp", ignore_errors=True)
        print ""

f = open("/home/bkallaher/runs/scores.json", 'w+')
json.dump(scores, f)
f.close()
