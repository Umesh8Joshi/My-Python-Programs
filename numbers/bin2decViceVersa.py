'''
	In this program we will create two separate functions
	First function will take decimal number and return binary
	Second function will take binary number and return decimal
'''

def bin2dec(bin):
	'''
	Function to convert binary to decimal
	:param bin: Binary number provided as a string
	:return: Integer in int data type\
	'''
	return int(bin, 2)

def dec2bin(dec):
	'''
	Function to convert dec to binary
	:param dec: decimal number in int form
	:return: Binary number in string form
	'''
	if dec > 1:
		dec2bin(n//2)
	return n%2