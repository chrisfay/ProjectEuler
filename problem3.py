#!/usr/bin/python

""" 
Project Euler
Problem #3

http://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def isPrime(num):
    #1 and below, no prime
    if num <= 1:
        return False

    #2 is the only even prime
    if num == 2:
        return True
    
    #Even number is not prime
    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False

    return True
   


largestPrime = 0
max = 600851475143

for i in range(1, int(math.sqrt(max))):
    #Is this number prime?  
    if isPrime(i) and max % i == 0:
        print str(i) + " is a prime number factor of " + str(max)
        largestPrime = i
    else:
        print str(i) + " nope. Current largest prime is " + str(largestPrime)
    
    i+=1

print "The largest prime factor of " + str(max) + " is " + str(largestPrime)    

   



