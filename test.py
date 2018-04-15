class Node:

	def __init__(self,val):
		self.val = val

class Tree:

	def __init__(self):
		self.root = 45


	def put(self,val):
		self.root = self._put(self.root,val)

	def _put(self,node,val):
		node = val
		return node

		


t = Tree()
t.put(23)
print(t.root)




