#MAX Heap

class Heap:

	HEAP_SIZE = 15
	def __init__(self):
		self.heap = [0]*Heap.HEAP_SIZE
		self.current_position  = -1

	def insert(self,item):

		if self.isFull():
			print('Heap is filled !! Cannot Insert')
			return

		self.current_position += 1
		self.heap[self.current_position] = item
		self.fix(self.current_position)

	# def fix(self,index):
	# 	parent = int((index-1)/2)
	# 	while parent >= 0 and self.heap[index]>self.heap[parent]:
	# 			t = self.heap[index]
	# 			self.heap[index] = self.heap[parent]
	# 			self.heap[parent] = t
	# 			parent = int((index-1)/2)


	def fix(self,index):
		
		while index > 0:
			parent = int((index-1)/2)
			if self.heap[index] > self.heap[parent]:
				t = self.heap[index]
				self.heap[index] = self.heap[parent]
				self.heap[parent] = t
				index = int((index-1)/2)
			else:
				index = int((index-1)/2)


	def isFull(self):
		if self.current_position == Heap.HEAP_SIZE-1:
			return True
		else:
			return False

#current position is the last index of the array
	def heapsort(self):
		for i in range(0,self.current_position+1):
			print(self.heap[0])
			self.heap[0],self.heap[self.current_position-i] = self.heap[self.current_position-i],self.heap[0]
			self.fixDown(1,self.current_position-i-1)

	def fixDown(self,index,upto):
		while index <= upto:
			parent = int((index-1)/2)
			if self.heap[index] > self.heap[parent]:
				self.heap[index],self.heap[parent] = self.heap[parent],self.heap[index]
				index += 1
			else:
				index += 1




h = Heap()
h.insert(10)
h.insert(-34)
h.insert(12)
h.insert(11)
h.insert(-7)
h.insert(56)
h.insert(1)
h.insert(-1)
h.insert(45)
h.insert(23)
h.insert(0)
h.insert(49)
h.insert(-20)
h.insert(2)


print(h.heap)
h.heapsort()

