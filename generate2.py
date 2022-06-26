#!/usr/bin/python3
import numpy 
def primes2(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return list(numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)])
primes = primes2(10000000)
print(primes)