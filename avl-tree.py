class Node:

	def __init__(self,data):

		self.data = data
		self.height = 0
		self.left = None
		self.right = None

class AVL:

	def __init__(self):
		self.root = None

	def calculateHeight(self,node):

		if not node:

			return -1

		return node.height
    
    #if it returns > 1 --- left heavy --> right rotation
    #if it returns < -1 --- right heavy --> left rotation
	def calculateBalance(self,node):

		if not node:

			return 0

		return self.calculateHeight(node.left)-self.calculateHeight(node.right)


	def rotateRight(self,node):

		print('Right rotation on ',node.data)
		tempLeftChild = node.left
		t = tempLeftChild.right
		tempLeftChild.right = node
		node.left = t

		node.height = max(self.calculateHeight(node.left),self.calculateHeight(node.right)) + 1
		tempLeftChild.height = max(self.calculateHeight(tempLeftChild.left),self.calculateHeight(tempLeftChild.right))+1

		return tempLeftChild



	def rotateLeft(self,node):

		print('Left rotation on ',node.data)
		tempRightChild = node.right
		t = tempRightChild.left
		tempRightChild.left = node
		node.right = t

		node.height = max(self.calculateHeight(node.left),self.calculateHeight(node.right)) + 1
		tempRightChild.height = max(self.calculateHeight(tempRightChild.left),self.calculateHeight(tempRightChild.right))+1

		return tempRightChild

	def insert(self,data):
		if self.root==None:
			self.root = Node(data)
		else:
			self.root = self._insert(data,self.root)


	def _insert(self,data,node):
		if data < node.data:
			if node.left == None:
				node.left = Node(data)
			else:
				node.left = self._insert(data,node.left)

		elif data > node.data:
			if node.right == None:
				node.right = Node(data)
			else:
				node.right = self._insert(data,node.right)

		else:
			print('attempt to add DUPLICATE value')

		node.height = max(self.calculateHeight(node.left),self.calculateHeight(node.right)) + 1

		return self.settleViolations(data,node)


	# def insert(self, data):
	# 	self.root = self.insertNode(data, self.root);
		
	# def insertNode(self, data, node):
	
	# 	if not node:
	# 		return Node(data);
			
	# 	if data < node.data:
	# 		node.left = self.insertNode(data, node.left);
	# 	else:
	# 		node.right = self.insertNode(data, node.right);
			
	# 	node.height = max( self.calculateHeight(node.left) , self.calculateHeight(node.right) ) + 1;
		
	# 	return self.settleViolations(data, node);


	def settleViolations(self,data,node):

		balance = self.calculateBalance(node)
		if balance > 1 and data < node.left.data:
			print('Left Left Heavy Situation')
			return self.rotateRight(node)

		
		if balance < -1 and data > node.right.data:
			print('Right Right Heavy Situation')
			return self.rotateLeft(node)

		
		if balance > 1 and data > node.left.data:
			print('Left Right Heavy Situation')
			node.left = self.rotateLeft(node.left)
			return self.rotateRight(node)
			

		if balance < -1 and data < node.right.data:
			print('Right Left Heavy Situation')
			node.right = self.rotateRight(node.right)
			return self.rotateLeft(node)
			
		return node

	def traverse(self):
		if self.root :
			self.traverseInorder(self.root)


	def traverseInorder(self,node):

		if node.left:
			self.traverseInorder(node.left)

		print(node.data)

		if node.right:
			self.traverseInorder(node.right)


avl = AVL()
# avl.insert(1)
# avl.insert(2)
# avl.insert(3)
# avl.insert(4)
# avl.insert(5)
# avl.insert(6)

# avl.insert(6)
# avl.insert(5)
# avl.insert(4)
# avl.insert(3)
# avl.insert(2)
# avl.insert(1)

avl.insert(3)
avl.insert(8)
avl.insert(5)

avl.traverse()



