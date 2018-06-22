'''
	This program will remove duplicates from List
	and will maintain the Order and return List
'''

def dedupe(items):
	'''Remove Dups and maintain Order'''
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)


'''
-> Working
>>> a = [1,2,3,4,1,2,6]
>>> list(dedupe(a))
[1,2,3,4,6]
'''