#!/usr/bin/env python

#Python 2.x fix
try: input = raw_input
except NameError: pass

n = int(input("Enter a number to be square rooted: "))

#def sqrt(n):
guess = n

while abs(guess*guess - n) > 0:
    guess = (guess +n/guess)/2.0
print (guess)


