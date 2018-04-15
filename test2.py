class Node:

	def __init__(self,val):
		self.val = val
		self.left = None


class Tree:

	def __init__(self):
		self.root = Node(1)

#self.root stores the address of Node(1)  ---> self.root = 2201
	def put(self,val):
		self._put(self.root,val)   #a copy of the address stored in self.root is passed

	def _put(self,node,val):
		node.val = val  #the address get changed in the copy of the self.root


#self.root stores the address of Node(1)
#

		

		


t = Tree()
t.put(23)
print(t.root.val)




