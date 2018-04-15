#binary search trees #O(log n) only if the tree is balanced

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class BinarySearchTree:

	def __init__(self):
		self.root = None


	def insert(self,data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insertNode(data,self.root)

	def insertNode(self,data,node):
		if data < node.data:
			if node.left:
				self.insertNode(data,node.left)
			else:
				node.left = Node(data)
		else:
			if node.right :
				self.insertNode(data,node.right)
			else:
				node.right = Node(data)



	def getMinVal(self):
		if self.root :
			return self.getMin(self.root)

	def getMin(self,node):
		if node.left:
			return self.getMin(node.left)
		
		return node.data

	def getMaxVal(self):
		if self.root:
			return self.getMax(self.root)


	def getMax(self,node):
		if node.right:
			return self.getMax(node.right)

		return node.data

	def traverse(self):
		if self.root:
			self.traverseInorder(self.root)

	def traverseInorder(self,node):
		if node.left:
			self.traverseInorder(node.left)

		print(node.data)


		if node.right:
			self.traverseInorder(node.right)

	# def traversePreorder(self,node):
	# 	print(node.data)

 #    	if node.left:
 #    		self.traversePreorder(node.left)

 #    	if node.right:
 #    		self.traversePreorder(node.right)


	def traversePostorder(self,node):

	    	if node.left:
	    		self.traversePostorder(node.left)

	    	if node.right:
	    		self.traversePostorder(node.right)

	    	print(node.data)
	
	def remove(self,data):

	    	if self.root != None:
	    		self.root = self.removeNode(data,self.root)

    
	def removeNode(self,data,node):
	    	if not node:
	    		return node

	    	if data < node.data:

	    		node.left = self.removeNode(data,node.left)
	    	elif data > node.data:

	    		node.right = self.removeNode(data,node.right)
	    	else:
	    		if not node.left and not node.right:
	    			print('leaf node')
	    			del node
	    			return None

	    		if not node.left:
	    			print('node with right child')
	    			tempNode = node.right
	    			del node
	    			return tempNode

	    		elif not node.right:
	    			print('node with left child')
	    			tempNode = node.left
	    			del node
	    			return tempNode

	    		print('Removing node with 2 children')
	    		tempNode = self.getPredecessor(node.left)
	    		node.data = tempNode.data
	    		node.left = self.removeNode(tempNode.data,node.left)

	    	return node



	def getPredecessor(self,node):
	    	if node.right:
	    		return self.getPredecessor(node.right)

	    	return node

    		










#inorder traversal
#1.left subtree
#2.root
#3.right subtree








bst  =  BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)
bst.remove(10)
print(bst.getMinVal())
print(bst.getMaxVal())



bst.traverse()