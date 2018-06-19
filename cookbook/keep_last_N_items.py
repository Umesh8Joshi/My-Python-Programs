'''
	This will keep only last N items from the
	text file by finding the pattern
'''
from collections import deque

def search(lines, pattern, history=5):
	'''A search function which will take lines and try to find patterns with N last lines'''
	previous_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)

def main():
	with open('anytext.txt') as f:
		for line, prevlines in search(f, 'python', 5):
			for pline in prevlines:
				print(pline, end='')
			print(line, end='')
			print('-'*20)

if __name__ == '__main__':
	main()