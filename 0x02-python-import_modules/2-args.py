#!/usr/bin/python3
import sys
arguments = sys.argv[1:]
n = len(arguments)
if n == 0:
    print("0  arguments.")
else:
    print("{} arguments:".format(n))
    for i, arg in enumerate(arguments, start=1):
        print("{}: {}".format(i, arg))
