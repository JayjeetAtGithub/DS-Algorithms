class Node:

	def __init__(self,key,val):
		self.val = val
		self.key = key
		self.next = None


class Hashmap:

	def __init__(self):
		self.size = 9
		self._map = [None]*self.size

	def _get_hash(self,key):
		hash = 0
		for char in str(key):
			hash += ord(char)
		return hash%self.size

	def add(self,key,val):

		key_hash = self._get_hash(key)
		newNode = Node(key,val)
		if self._map[key_hash] == None:
			self._map[key_hash] = newNode
		else:
			root = self._map[key_hash]
			if root.key == key:
				root.val = val
				return
			while(root.next != None):
				if root.key == key:
					root.val = val
					return
				root = root.next
			root.next = newNode


	def get(self,key):
		key_hash = self._get_hash(key)
		if self._map[key_hash] != None:
			root = self._map[key_hash]
			while(root.key != key):
				root = root.next
				if root == None:
					return None
			return root.val

		return None



	

h = Hashmap()
h.add('w',23)
h.add('name',"jayjeet")
h.add('name','ankan')
h.add('name',7)
h.add('anme',"souvik")
print(h.get('ag'))
print(h.get('name'))
print(h.get('anme'))
print(h.get('naem'))
print(h.get('w'))