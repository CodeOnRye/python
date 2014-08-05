#!/usr/bin/env python

#32 bit division
def divide(dividend, divisor):
    quotient = 0
    remainder = dividend
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
    return (quotient, remainder)
    
#main program
print (divide(125,7))
