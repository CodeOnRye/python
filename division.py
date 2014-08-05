#!/usr/bin/env python

#int quotient
#int remainder
#Python 2.x fix
try: input = raw_input
except NameError: pass

dividend = int(input("What is the dividend? "))
divisor = int(input("What is the dvisor? "))

#32 bit division
def divide(dividend, divisor):
    quotient = 0
    remainder = dividend
    divisorOriginal = divisor
    #shift left 32 bits
    #makes it 64 bits
    divisor = divisor << 32
    
    #n+1 iterations
    for i in range(33):
        if divisor < remainder:
            #shift left and or in a 1
            quotient = (quotient << 1) | 1
            remainder = remainder - divisor
        else:
            #shift left, no need to or in a 0
            quotient = quotient << 1
        divisor = divisor >> 1

    if remainder == divisorOriginal:
        quotient = quotient + 1
        remainder = 0


#    print (quotient, remainder)
    return (quotient, remainder)
    
#main program
print (divide(dividend,divisor))
