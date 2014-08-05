
def multiply(multiplicand,multiplier):

	product = 0
	
	#check for neg/pos, returns true
	multiplicand_pos = (multiplicand & 0x80000000 == 0) 
	multiplier_pos = (multiplier & 0x80000000 == 0) 

	if not multiplicand_pos:
		#~ is bitwise invert
		multiplicand = ~multiplicand + 1
	if not multiplier_pos:
		multiplier = ~multiplier + 1

	#32 bits
	for i in range(32):
		if multiplier & 1 == 1:
			product = product + multiplicand
	
		#shift right
		multiplicand = multiplicand << 1
		#shift left
		multiplier = multiplier >> 1
	
	# != is the same as exclusive or	
	if multiplicand_pos != multiplier_pos:
		product = ~product + 1

	
	return product

print multiply(8,-9)
