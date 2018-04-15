#Linked List

class Node(object):

	def __init__(self,data):
		self.data = data
		self.next = None


class LinkedList(object):
                       
	def __init__(self):
		self.root = None
		self.size = 0


	def insertStart(self,data):
		self.size = self.size + 1
		newNode = Node(data)

		if not self.root:
			self.root = newNode
		else:
			newNode.next = self.root
			self.root = newNode


	# O(1)


	def sizel(self):
		return self.size

	def traverse(self):
		head = self.root
		while head != None:
			print(head.data)
			head = head.next


	def insertEnd(self,data):
		head = self.root
		newNode = Node(data)
		while head.next != None:
			head = head.next

		head.next = newNode


	def insertPosition(self,pos,data):
		if pos == 0:
			self.size = self.size + 1
			newNode = Node(data)

			if not self.root:
				self.root = newNode
			else:
				newNode.next = self.root
				self.root = newNode

		else:

			previousNode = None
			head = self.root
			for i in range(0,pos):
				previousNode = head
				head = head.next
			newNode = Node(data)
			newNode.next = head
			previousNode.next = newNode




	def remove(self,data):

		if self.root is None:
			return
		
		self.size = self.size - 1
		currentNode = self.root
		previousNode = None
		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.next

		if previousNode is None:
			self.root = currentNode.next
		else:
			previousNode.next = currentNode.next
			del currentNode






l = LinkedList()

l.insertStart(122)
l.insertStart(78)
l.insertStart(10)
# l.traverse()
# l.remove(10)
# l.remove(122)
# l.traverse()
l.insertEnd(4)
l.insertPosition(4,45)

l.traverse()
# l.insertEnd(56)
# l.insertEnd(10)

#print(l.sizel())