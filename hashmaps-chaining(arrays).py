#Hash maps have O(1) complexity
#Array
#Hash Function
#Collision Handling

class Hashmap:

	def __init__(self):
		self.size = 6
		self.map = [None] * self.size

	def _get_hash(self,key):
		hash = 0
		for char in str(key):
			hash += ord(char)

		return hash % self.size


	def add(self,key,val):
		key_hash = self._get_hash(key)
		key_value = [key,val]
		if self.map[key_hash] is None:
			self.map[key_hash] = list([key_value])
			return True
		else:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					pair[1] ==val
					return True

			self.map[key_hash].append(key_value)
			return True


	def get(self,key):
		key_hash = self._get_hash(key)
		if self.map[key_hash] != None:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]

		return None


	def delete(self,key):

		key_hash = self._get_hash(key)
		if self.map[key_hash] == None :
			return False
		for i in range(0,len(self.map[key_hash])):
			if self.map[key_hash][i][0] == key:
				self.map[key_hash].pop(i)
				return True

	def traverse(self):
		for item in self.map:
			if item != None:
				print(str(item))



h = Hashmap()

h.add('bob',34)
h.add('jaya',90)
h.add('ankan',45)
print(h.get('bob'))
print(h.get('jaya'))
h.delete('jaya')
print(h.get('jaya'))
h.traverse()

