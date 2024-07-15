# provided, could be named "BST", feel free to edit
class node:

	# provided, feel free to edit
	def __repr__(self):
		lstr = ""
		mstr = ""
		if self.less != None:
			lstr = "(" + self.less.__repr__() + ") <- "
		if self.more != None:
			mstr = " -> (" + self.more.__repr__() + ")"
		return lstr + str(self.data) + mstr
	
	# provided, feel free to edit
	def __str__(self):
		return self.__repr__()

	# provided, feel free to edit
	def __init__(self, d, l=None, m=None):
		self.data = d # piece of data (not None)
		self.less = l # None or another node
		self.more = m # None or another node
		
	# calculate size of the BST - the number of elements it contains
	# * always greater than zero
	def size(self):
		if self.data == None:
			return 0
		if self.less and self.more:
			return 1 + self.less.size() + self.more.size()
		if self.less:
			return 1 + self.less.size()
		if self.more:
			return 1 + self.more.size()
		return 1
		
	# calculate size of the BST - the number of elements in the longest single path
	# * always greater than zero	
	def depth(self):
		if self.data == None:
			return 0
		if self.more and self.less:
			return 1 + max(self.less.depth(),self.more.depth())
		if self.more:
			return 1 + self.more.depth()
		if self.less:
			return 1 + self.less.depth()
		return 1

	# given d, return the BST containing all elements in the BST and also d
	# * may ignore the case of duplicates, like adding "2" twice
	# * may assume added elements are of comparable types
	def insert(self, d):
		if d < self.data:
			if not self.less:
				self.less = node(d)
			else:
				self.less = self.less.insert(d)
		if d > self.data:
			if not self.more:
				self.more = node(d)
			else: 
				self.more = self.more.insert(d)
		return self

	# given d, return true if d is in the BST
	# * may assume added elements are of comparable types		
	def contains(self, d):
		data, less, more = self.data, self.less, self.more
		if data == d:
			return True
		if more and more.contains(d):
			return True
		if less and less.contains(d):
			return True
		return False
	
	def find(self, d):
		if self.data == d:
			return self.data
		if self.more and self.more.find(d):
			return self.more.find(d)
		if self.less and self.less.find(d):
			return self.less.find(d)
		
	# return the minimum value in the bst
	def getMin(self):
		if self.less:
			return self.less.getMin()
		return self.data
	
	# return the maximum value in the bst
	def getMax(self):
		if self.more:
			return self.more.getMax()
		return self.data
			
	# given d, return the BST containing all elements in the BST except d
	# * may ignore the case of duplicates
	# * may assume elements are of comparable types
	def remove(self, d):
		if d < self.data and self.less:
			self.less = self.less.remove(d)
		if d > self.data and self.more:
			self.more = self.more.remove(d)
		if d == self.data:
			if self.less:
				self.data = self.less.getMax()
				self.less = self.less.remove(self.less.getMax())
			elif self.more:
				self.data = self.more.getMin()
				self.more = self.more.remove(self.more.getMin())
			else:
				self = None
		return self

		
		
# provided as a curiousity, an outer class to wrap node and allow BSTs to be of size zero
# feel free to edit
class BST:
	
	def __repr__(self):
		return "BST: " + self.node.__repr__()
	
	def __str__(self):
		return "BST: " + self.node.__str__()

	def __init__(self, d=None):
		if d == None:
			self.node = None # always a node or None
		else:
			self.node = node(d) # always a node or None
		
	def size(self):
		if self.node == None:
			return 0
		return self.node.size()
	
	def depth(self):
		if self.node == None:
			return 0
		return self.node.depth()
	
	# this returns self for the autograder as a convenience
	def insert(self, d):
		if self.node == None:
			self.node = node(d)
		else:
			self.node.insert(d)
		return self
		
	def contains(self, d):
		if self.node == None:
			return False
		return self.node.contains(d)
	
	# returns None if the BST contains no min
	def getMin(self):
		if self.node == None:
			return
		return self.node.getMin()
	
	def find(self, d):
		if self.node == None:
			return
		return self.node.find(d)
	# returns None if the BST contains no max
	def getMax(self):
		if self.node == None:
			return
		return self.node.getMax()
	
	# this returns self for the autograder as a convenience
	def remove(self, d):
		if self.node == None:
			return
		self.node = self.node.remove(d)
		return self
	