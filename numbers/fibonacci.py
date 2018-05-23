#Enter a number to find the fibonacci sequence till date

def fib(n):
	'''
	Function will return fibonacci sequence
	:param n: number of sequence entered by user
	:return: The sequence to that number
	'''
	if n < 2: return
	else: return fib(n-1) + fib(n-2)

def main():
	n = input('Enter the nunber')
	print(fib(n))
	#we are using recursion here

if __name__ == "__main__":
	main()