#Defining the node

class Node:

	def __init__(self,data):
		self.data = data
		self.next = None


class CircularLinkedList:

	def __init__(self):
		self.root = None


	def length(self):
		current = self.root
		if current == None:
			return 0

		count = 1
		current = current.next
		while current != self.root:
			current = current.next
			count += 1

		return count


	def display_clinkedlist(self):
		current = self.root
		if current == None:
			return 0

		print(current.data)
		current = current.next
		while current != self.root:
			print(current.data)
			current = current.next


	def insertAtEnd(self,val):
		if self.root == None:
			newNode = Node(val)
			self.root = newNode
			self.root.next = self.root
		else:
			current = self.root
			newNode = Node(val)
			while current.next != self.root:
				current = current.next

			current.next = newNode
			newNode.next = self.root


	def insertAtBeg(self,val):
		if self.root == None:
			newNode = Node(val)
			self.root = newNode
			self.root.next = self.root
		else:
			current = self.root
			while current.next != self.root:
				current = current.next    #it is now the last node
			newNode = Node(val)
			newNode.next = self.root
			current.next = newNode
			self.root = newNode

	def deleteFromEnd(self):
		if self.root == None:
			print('CircularLinkedList is Empty')
			return

		current = self.root
		prev = self.root
		while current.next != self.root:
			temp = current
			current = current.next

		temp.next = current.next
		del current

	def deleteFromStart(self):
		if self.root == None:
			print('CircularLinkedList is Empty')
			return

		current = self.root
		while current.next != self.root:
			current = current.next

		current.next = self.root.next
		t = self.root
		self.root = t.next
		del t  



cll = CircularLinkedList()
cll.insertAtEnd(12)
cll.insertAtEnd(14)
cll.insertAtEnd(5)
cll.deleteFromStart()
cll.insertAtBeg(122)
cll.insertAtBeg(56)
cll.deleteFromEnd()
cll.deleteFromStart()
print(cll.length())
cll.display_clinkedlist()


