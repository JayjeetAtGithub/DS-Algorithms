class Queue:

	def __init__(self):

		self.queue = []

	def isEmpty(self):
		return self.queue == []

	def enqueue(self,data):

		self.queue.append(data)

	def dequeue(self):

		data = self.queue[0]
		del self.queue[0]
		return data

	def peek(self):

		return self.queue[0]

	def size(self):

		return len(self.queue)



q =Queue()
q.enqueue(10)
q.enqueue(23)
q.enqueue(67)
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.peek())
q.enqueue(56)
print(q.isEmpty())
print(q.size())