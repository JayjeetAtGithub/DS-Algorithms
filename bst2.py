from queues import Queue

class Node:
	def __init__(self,val):
		self.val = val
		self.left_child = None
		self.right_child = None

class BST:

	def __init__(self):
		self.root = None

	def insert(self,data):
		if self.root==None:
			self.root = Node(data)
		else:
			self._insert(data,self.root)


	def _insert(self,data,node):
		if data < node.val:
			if node.left_child == None:
				node.left_child = Node(data)
			else:
				self._insert(data,node.left_child)

		elif data > node.val:
			if node.right_child == None:
				node.right_child = Node(data)
			else:
				self._insert(data,node.right_child)

		else:
			print('attempt to add DUPLICATE value')


	def traverseInorder(self):
		if self.root != None:
			self._traverse(self.root)

	def _traverse(self,node):
		if node!=None:
			self._traverse(node.left_child)
			print(node.val)
			self._traverse(node.right_child)


	def height(self):
		if self.root!=None:
			return self._height(self.root,0)
		else:
			return 0

	def _height(self,node,h):
		if node == None:
			return h

		left_height = self._height(node.left_child,h+1)
		right_height = self._height(node.right_child,h+1)
		if left_height>right_height:
			return left_height
		else:
			return right_height

	def search(self,value):
		if self.root != None:
			return self._search(self.root,value)
		else:
			return False

	def _search(self,node,value):
		if value == node.val:
			return True
		elif value < node.val and node.left_child != None:
			return self._search(node.left_child,value)
		elif value > node.val and node.right_child != None:
			return self._search(node.right_child,value)
		else:
			return False

	def depth(self,value):
		if self.root == None:
			return -1
		else:
			return self._depth(value,self.root,0)


	def _depth(self,value,node,depth):
        
		if value < node.val:
			return self._depth(value,node.left_child,depth+1)
		elif value > node.val:
			return self._depth(value,node.right_child,depth+1)
		else:
			return depth


	def levelOrderTraversal(self,result):
		rootNode = self.root
		q = Queue()
		q.enqueue(rootNode)
		node = None

		while not q.isEmpty():
			node = q.dequeue()
			result.append(node.val)

			if node.left_child != None:
				q.enqueue(node.left_child)

			if node.right_child != None:
				q.enqueue(node.right_child)

		return result





tree = BST()
tree.insert(10)
tree.insert(12)
tree.insert(7)
tree.insert(18)
tree.insert(11)
tree.insert(4)
tree.insert(9)
tree.traverseInorder()
print('Tree height:',tree.height())
print(tree.search(9))
print(tree.search(12))
print('------------------------')
print(tree.depth(10))
print(tree.height())
print('---level order traversal---')
result = []
print(tree.levelOrderTraversal(result))

