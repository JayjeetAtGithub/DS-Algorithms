class Node:

	def __init__(self,name):

		self.name = name
		self.adjacenciesList = []
		self.visited = False
		self.predecessor = None


class DFS:

	def dfs(self,node):

		node.visited = True
		print(node.name)

		for n in node.adjacenciesList:

			if not n.visited:
				self.dfs(n)



node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')
node5 = Node('e')

node1.adjacenciesList.append(node2)
node1.adjacenciesList.append(node3)
node2.adjacenciesList.append(node4)
node4.adjacenciesList.append(node5)

dfs = DFS()
dfs.dfs(node1)

