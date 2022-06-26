#!/usr/bin/python3
import sys
with open('tests/test01', 'w') as f:
    for i in range(int(sys.argv[1]), int(sys.argv[1]) + 10000):
        f.write(str(i))
        f.write('\n')
    exit
