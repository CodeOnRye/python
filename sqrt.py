#!/usr/bin/env python

#Python 2.x fix
try: input = raw_input
except NameError: pass

n = int(input("Enter a number to be square rooted: "))

#def sqrt(n):
root_value = n

while abs( root_value * root_value - n) > 0:
    root_value_old = root_value
    root_value = (root_value + n / root_value) / 2.0
    if root_value_old == root_value:
       print ("There is no square root!")
       exit()

print ("The sqare root of %d is %d!" % (n, root_value))


