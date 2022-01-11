#!/usr/local/bin/python3

import os
import sys

def get_args():
    return sys.argv[1:]


def history():
    lines = os.popen('git log').read().splitlines()
    commits = [line.split(" ")[1]
               for line in lines if line.startswith("commit")]

    return commits


def get_files(endings):
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if len([e for e in endings if name.endswith(e)]) > 0:
                yield root + "/" + name


def linecount(filename):
    file1 = open(filename, 'r')
    lines = file1.readlines()
    return sum([1 for line in lines])


def checkout(commit):
    os.system("git checkout " + commit)


files = get_args()

count = []

for commit in history():
    checkout(commit)
    counts = [linecount(file) for file in get_files(files)]
    total = sum(counts)
    count.insert(0, total)

for c in count:
    print(c)

