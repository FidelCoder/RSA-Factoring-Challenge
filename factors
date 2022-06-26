#!/usr/bin/python3
import sys
import subprocess as sp


def factors(n):
    step = 2 if n % 2 == 0 else 1
    return [i for i in range(2, int(n**0.5) + 1, step) if n % i == 0]


def factors2(public):
    i = (int(public))
    str2 = "factor " + str(i)
    output = sp.getoutput(str2)
    y = output.split()
    print("{}={}*{}".format(y[0][:-1], int(y[0][:-1])//int(y[1]), y[1]))


with open(sys.argv[1]) as file:
    x = list(map(factors2, [line.strip() for line in file]))
