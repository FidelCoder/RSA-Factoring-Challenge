#!/usr/bin/python3
import sys
from functools import reduce
def factors2(public):
        i = (int(public))
        for count in range(2, int(i**0.5) + 1):
            if i % count == 0:
                return [i, i // count, count]
            else:
                continue

def printf(listd):
        if (listd):
            print("{}={}*{}".format(listd[0], listd[1] , listd[2]))
        

with open(sys.argv[1]) as file:
        list(map(printf,list(map(factors2, [line.strip() for line in file]))))