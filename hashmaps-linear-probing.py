class HashMap:

	def __init__(self):
		self.size = 10
		self.keys = [None] * self.size
		self.values = [None] * self.size


	def hashfunction(self,key):
		sum = 0
		for pos in range(len(key)):
			sum = sum + ord(key[pos])

		return sum%self.size


	def put(self,key,data):

		index = self.hashfunction(key)

		while self.keys[index] != None:
			if self.keys[index] == key:
				self.values[index]=data
				return

			index = (index+1)%self.size

		self.keys[index] = key
		self.values[index] = data


	def get(self,key):

		index = self.hashfunction(key)
		while self.keys[index] != None:
			if self.keys[index] == key:
				return self.values[index]

			index = (index+1)%self.size

		return None

h = HashMap()
h.put('a',12)
h.put('c',23)
print(h.get('c'))
	