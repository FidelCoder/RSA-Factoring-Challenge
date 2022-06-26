#!/usr/bin/python3
import sys


def factors(n):
    step = 2 if n % 2 == 0 else 1
    return [i for i in range(2, int(n**0.5) + 1, step) if n % i == 0]

def factors2(public):
        i = (int(public))
        for count in range(2, int(i**0.5) + 1):
            if i % count == 0:
                print("{}={}*{}".format(i, i // count, count))
                i = 0
                break
            else:
                continue
        if i !=0:
               print("{}={}*{}".format(i, i, 1))
        

with open(sys.argv[1]) as file:
        x = list(map(factors2, [line.strip() for line in file]))
