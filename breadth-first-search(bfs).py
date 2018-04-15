class Node:

	def __init__(self,name):
		self.name = name
		self.visited = False
		self.adjacencyList=[]
		self.predecessor = None


class BFS:

	def bfs(self,startNode):

		queue = []
		queue.append(startNode)
		startNode.visited = True

		while queue:
			actualNode = queue.pop(0)
			print(actualNode.name)

			for n in actualNode.adjacencyList:
				if not n.visited:
					n.visited = True
					queue.append(n)



node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)

bfs = BFS()
bfs.bfs(node1)


#BFS -> Queue