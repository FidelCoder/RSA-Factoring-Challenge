#!/usr/bin/python3
import sys
with open(sys.argv[1]) as file:
    for line in file:
        i = (int(line.rstrip()))
        for count in range(2, int(i**0.5) + 1):
            if i % count == 0:
                print("{}={}*{}".format(i, i // count, count))
                i = 0
                break
            else:
                continue

