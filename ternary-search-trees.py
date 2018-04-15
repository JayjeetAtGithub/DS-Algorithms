#Using ternary search trees as a dictionary / hashmap

class Node:

	def __init__(self,character):
		self.character = character
		self.left=None
		self.right=None
		self.middle=None
		self.value=0


class TST:

	def __init__(self):
		self.root = None

	def put(self,key,value):

		self.root = self._put(self.root,key,value,0)

	def _put(self,node,key,value,index):

		c = key[index]
		if node == None:
			node = Node(c)


		if c < node.character:
			node.left = self._put(node.left,key,value,index)

		elif c > node.character:
			node.right = self._put(node.right,key,value,index)

		elif index < len(key)-1:
			node.middle = self._put(node.middle,key,value,index+1)

		else:
			node.value = value

		return node




	def get(self,key):

		node = self._get(self.root,key,0)
		if node == None:
			return -1
		else:
			return node.value

	def _get(self,node,key,index):

		if node == None:
			return None

		c = key[index]
		if c < node.character:
			return self._get(node.left,key,index)

		elif c > node.character:
			return self._get(node.right,key,index)

		elif index < len(key)-1:
			return self._get(node.middle,key,index+1)

		else:
			return node





tst = TST()
tst.put('car',12)
tst.put('abc',11)
tst.put('bcd',34)
print(tst.get('abc'))
print(tst.get('bcd'))
print(tst.get('car'))
print(tst.get('www'))




