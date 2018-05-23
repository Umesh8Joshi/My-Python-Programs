'''
Enter a number to find the value of PI till that digit
'''

def nthPI(num):
	'''
	function to return nth digit value of PU
	:param num: number provided by user
	:return : PI value till that digit
	'''

	num = input('Enter the digit')
	return "%.{num}f"(22/7).format(num)