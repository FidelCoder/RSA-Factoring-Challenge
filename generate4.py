#!/usr/bin/python3
import sys
import subprocess as sp


x = ""
with open(sys.argv[1]) as file: 
        x = file.readline().rstrip()
        str2 = "factor " + str(x)
        output = sp.getoutput(str2)
        y = output.split()
        if len(y) == 3:
            print("{}={}*{}".format(y[0][:-1],
                  int(y[0][:-1])//int(y[1]), y[1]))
        else:
            pass
