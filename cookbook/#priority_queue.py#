'''A queue that sorts items by a given priority'''

import heapq

class  PriorityQueue(object):
	"""PriorityQueue will pop items based on priority assigned"""
	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self, item, priority):
		'''Insert data into a List with Priority'''
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1

	def pop(self):
		'''Pop data with highest priority'''
		return heapq.heappop(self._queue)[-1]
'''
Usage:
in python terminal
>>> from priority_queue import PriorityQueue
>>> a = PriorityQueue()
>>> a.push('name', 1) # 1 is priority
>>> a.push('random', 2)
>>> a.push('umesh', 3)
>>> a.pop() # highest priority will be pop first
'umesh'
'''