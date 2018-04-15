class Node:

	def __init__(self,data):
		self.data = data
		self.prev = None
		self.next = None

class DLL:

	def __init__(self):
		self.root = None

	def insertBeginning(self,data):
		if self.root == None:
			newNode = Node(data)
			self.root = newNode
		else:
			newNode = Node(data)
			rootnode = self.root
			newNode.next = rootnode
			rootnode.prev = newNode
			self.root = newNode

	def insertEnd(self,data):
		
		if self.root == None:
			newNode = Node(data)
			self.root = newNode
		else:
			prevnode = self.root
			while(prevnode.next != None):
				prevnode = prevnode.next

			newNode = Node(data)
			prevnode.next = newNode
			newNode.prev = prevnode


	def traverse(self):
		rootnode = self.root
		while(rootnode.next != None):
			print(rootnode.data)
			rootnode = rootnode.next
		print(rootnode.data)


	def removeBeg(self):

		temp = self.root
		self.root = temp.next
		self.root.prev = None
		del temp

	def removeEnd(self):

		rootnode = self.root
		while(rootnode.next != None):
			rootnode = rootnode.next

		prevnode = rootnode.prev
		prevnode.next = None
		rootnode.prev = None
		del rootnode
		del prevnode

	def removeBetween(self,val):

		rootnode = self.root
		while(rootnode.data != val):
			rootnode = rootnode.next
		prevnode = rootnode.prev
		prevnode.next = rootnode.next
		rootnode.next.prev = prevnode
		del rootnode

	def insertAtPosition(self,pos,val):

		rootnode = self.root
		for i in range(0,pos):
			rootnode = rootnode.next
		prevnode = rootnode.prev	
		newNode = Node(val)
		newNode.next = rootnode
		rootnode.prev = newNode
		prevnode.next = newNode
		newNode.prev = prevnode





dll = DLL()
#dll.insertBeginning(20)
dll.insertEnd(15)
dll.insertEnd(11)
dll.insertBeginning(67)
dll.insertBeginning(13)
dll.insertBeginning(56)
dll.insertEnd(87)
dll.removeEnd()
dll.removeEnd()
dll.removeBeg()
dll.removeBetween(67)
dll.insertAtPosition(1,1000)
# dll.removeBetween(11)
# dll.removeBetween(67)
# dll.removeBetween(15)
# dll.traverse()
#dll.removeBeg()
#dll.removeBeg()
#dll.traverse()
#dll.insertAtPosition(3,100)
dll.traverse()

