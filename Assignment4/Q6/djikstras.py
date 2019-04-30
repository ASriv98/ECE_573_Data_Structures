from collections import deque, namedtuple, defaultdict


# # # we'll use infinity as a default distance to nodes.
# # inf = float('inf')
# # Edge = namedtuple('Edge', 'start, end, cost')


# # def make_edge(start, end, cost=1):
# #   return Edge(start, end, cost)


# # class Graph:
# #     def __init__(self, edges):
# #         # let's check that the data is right
# #         wrong_edges = [i for i in edges if len(i) not in [2, 3]]
# #         if wrong_edges:
# #             raise ValueError('Wrong edges data: {}'.format(wrong_edges))

# #         self.edges = [make_edge(*edge) for edge in edges]

# #     @property
# #     def vertices(self):
# #         return set(
# #             sum(
# #                 ([edge.start, edge.end] for edge in self.edges), []
# #             )
# #         )

# #     def get_node_pairs(self, n1, n2, both_ends=True):
# #         if both_ends:
# #             node_pairs = [[n1, n2], [n2, n1]]
# #         else:
# #             node_pairs = [[n1, n2]]
# #         return node_pairs

# #     def remove_edge(self, n1, n2, both_ends=True):
# #         node_pairs = self.get_node_pairs(n1, n2, both_ends)
# #         edges = self.edges[:]
# #         for edge in edges:
# #             if [edge.start, edge.end] in node_pairs:
# #                 self.edges.remove(edge)

# #     def add_edge(self, n1, n2, cost=1, both_ends=True):
# #         node_pairs = self.get_node_pairs(n1, n2, both_ends)
# #         for edge in self.edges:
# #             if [edge.start, edge.end] in node_pairs:
# #                 return ValueError('Edge {} {} already exists'.format(n1, n2))

# #         self.edges.append(Edge(start=n1, end=n2, cost=cost))
# #         if both_ends:
# #             self.edges.append(Edge(start=n2, end=n1, cost=cost))

# #     @property
# #     def neighbours(self):
# #         neighbours = {vertex: set() for vertex in self.vertices}
# #         for edge in self.edges:
# #             neighbours[edge.start].add((edge.end, edge.cost))

# #         return neighbours

# #     def dijkstra(self, source, dest):
# #         assert source in self.vertices, 'Such source node doesnt exist'
# #         distances = {vertex: inf for vertex in self.vertices}
# #         previous_vertices = {
# #             vertex: None for vertex in self.vertices
# #         }
# #         distances[source] = 0
# #         vertices = self.vertices.copy()

# #         while vertices:
# #             current_vertex = min(
# #                 vertices, key=lambda vertex: distances[vertex])
# #             vertices.remove(current_vertex)
# #             if distances[current_vertex] == inf:
# #                 break
# #             for neighbour, cost in self.neighbours[current_vertex]:
# #                 alternative_route = distances[current_vertex] + cost
# #                 if alternative_route < distances[neighbour]:
# #                     distances[neighbour] = alternative_route
# #                     previous_vertices[neighbour] = current_vertex

# #         path, current_vertex = deque(), dest
# #         while previous_vertices[current_vertex] is not None:
# #             path.appendleft(current_vertex)
# #             current_vertex = previous_vertices[current_vertex]
# #         if path:
# #             path.appendleft(current_vertex)
# #         return path


# # #graph = Graph([
# # #    ("4", "5", 0.35),  ("5", "4", -0.66),  ("4", "7", 0.37), ("5", "7", 0.28),
# # #    ("7", "5", 0.28), ("5", "1", 0.32), ("0", "4", 0.38),  ("0", "2", 0.26),
# # #    ("7", "3", 0.39), ("1", "3", 0.29), ("2", "7", 0.34), ("6", "2", 0.40), ("3", "6", 0.52), ("6", "0", 0.58), ("6", "4", 0.93)])

# # graph = Graph([
# #     ("4", "5", 0.35),  ("5", "4", -0.66),  ("4", "7", 0.37), ("5", "7", 0.28),
# #     ("7", "5", 0.28), ("5", "1", 0.32), ("0", "4", 0.38),  ("0", "2", 0.26),
# #     ("7", "3", 0.39), ("1", "3", 0.29), ("2", "7", 0.34), ("6", "2", -1.20), ("3", "6", 0.52), ("6", "0", -1.40), ("6", "4", -1.25)])

# # print(graph.dijkstra("0", "4"))

# # A Python program for Dijkstra's shortest  
# # path algorithm for adjacency 
# # list representation of graph 
  
# from collections import defaultdict 
# import sys 
  
# class Heap(): 
  
# 	def __init__(self): 
# 		self.array = [] 
# 		self.size = 0
# 		self.pos = [] 
  
# 	def newMinHeapNode(self, v, dist): 
# 		minHeapNode = [v, dist] 
# 		return minHeapNode 
  
# 	# A utility function to swap two nodes  
# 	# of min heap. Needed for min heapify 
# 	def swapMinHeapNode(self,a, b): 
# 		t = self.array[a] 
# 		self.array[a] = self.array[b] 
# 		self.array[b] = t 
  
# 	# A standard function to heapify at given idx 
# 	# This function also updates position of nodes  
# 	# when they are swapped.Position is needed  
# 	# for decreaseKey() 
# 	def minHeapify(self, idx): 
# 		smallest = idx 
# 		left = 2*idx + 1
# 		right = 2*idx + 2
  
# 		if left < self.size and self.array[left][1]  < self.array[smallest][1]: 
# 			smallest = left 
  
# 		if right < self.size and self.array[right][1] < self.array[smallest][1]: 
# 			smallest = right 
  
# 		# The nodes to be swapped in min  
# 		# heap if idx is not smallest 
# 		if smallest != idx: 
  
# 			# Swap positions 
# 			self.pos[ self.array[smallest][0] ] = idx 
# 			self.pos[ self.array[idx][0] ] = smallest 
  
# 			# Swap nodes 
# 			self.swapMinHeapNode(smallest, idx) 
  
# 			self.minHeapify(smallest) 
  
# 	# Standard function to extract minimum  
# 	# node from heap 
# 	def extractMin(self): 
  
# 		# Return NULL wif heap is empty 
# 		if self.isEmpty() == True: 
# 			return
  
# 		# Store the root node 
# 		root = self.array[0] 
  
# 		# Replace root node with last node 
# 		lastNode = self.array[self.size - 1] 
# 		self.array[0] = lastNode 
  
# 		# Update position of last node 
# 		self.pos[lastNode[0]] = 0
# 		self.pos[root[0]] = self.size - 1
  
# 		# Reduce heap size and heapify root 
# 		self.size -= 1
# 		self.minHeapify(0) 
  
# 		return root 
  
# 	def isEmpty(self): 
# 		return True if self.size == 0 else False
  
# 	def decreaseKey(self, v, dist): 
  
# 		# Get the index of v in  heap array 
  
# 		i = self.pos[v] 
  
# 		# Get the node and update its dist value 
# 		self.array[i][1] = dist 
  
# 		# Travel up while the complete tree is  
# 		# not hepified. This is a O(Logn) loop 
# 		while i > 0 and self.array[i][1] < self.array[(i - 1) / 2][1]: 
  
# 			# Swap this node with its parent 
# 			self.pos[ self.array[i][0] ] = (i-1)/2
# 			self.pos[ self.array[(i-1)/2][0] ] = i 
# 			self.swapMinHeapNode(i, (i - 1)/2 ) 
  
# 			# move to parent index 
# 			i = (i - 1) / 2; 
  
# 	# A utility function to check if a given  
# 	# vertex 'v' is in min heap or not 
# 	def isInMinHeap(self, v): 
  
# 		if self.pos[v] < self.size: 
# 			return True
# 		return False
  
  
# def printArr(dist, n): 
# 	print "Vertex\tDistance from source"
# 	for i in range(n): 
# 		print "%d\t\t%d" % (i,dist[i]) 
  
  
# class Graph(): 
  
# 	def __init__(self, V): 
# 		self.V = V 
# 		self.graph = defaultdict(list) 
  
# 	# Adds an edge to an undirected graph 
# 	def addEdge(self, src, dest, weight): 
  
# 		# Add an edge from src to dest.  A new node  
# 		# is added to the adjacency list of src. The  
# 		# node is added at the begining. The first  
# 		# element of the node has the destination  
# 		# and the second elements has the weight 
# 		newNode = [dest, weight] 
# 		self.graph[src].insert(0, newNode) 
  
# 		# Since graph is undirected, add an edge  
# 		# from dest to src also 
# 		newNode = [src, weight] 
# 		self.graph[dest].insert(0, newNode) 
  
# 	# The main function that calulates distances  
# 	# of shortest paths from src to all vertices.  
# 	# It is a O(ELogV) function 
# 	def dijkstra(self, src): 
  
# 		V = self.V  # Get the number of vertices in graph 
# 		dist = []   # dist values used to pick minimum  
# 					# weight edge in cut 
  
# 		# minHeap represents set E 
# 		minHeap = Heap() 
  
# 		#  Initialize min heap with all vertices.  
# 		# dist value of all vertices 
# 		for v in range(V): 
# 			dist.append(sys.float_info.max) 
# 			minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]) ) 
# 			minHeap.pos.append(v) 
  
# 		# Make dist value of src vertex as 0 so  
# 		# that it is extracted first 
# 		minHeap.pos[src] = src 
# 		dist[src] = 0
# 		minHeap.decreaseKey(src, dist[src]) 
  
# 		# Initially size of min heap is equal to V 
# 		minHeap.size = V; 
  
# 		# In the following loop, min heap contains all nodes 
# 		# whose shortest distance is not yet finalized. 
# 		while minHeap.isEmpty() == False: 
  
# 			# Extract the vertex with minimum distance value 
# 			newHeapNode = minHeap.extractMin() 
# 			u = newHeapNode[0] 
  
# 			# Traverse through all adjacent vertices of  
# 			# u (the extracted vertex) and update their  
# 			# distance values 
# 			for pCrawl in self.graph[u]: 
  
# 				v = pCrawl[0] 
  
# 				# If shortest distance to v is not finalized  
# 				# yet, and distance to v through u is less  
# 				# than its previously calculated distance 
# 				if minHeap.isInMinHeap(v) and dist[u] != sys.maxint and pCrawl[1] + dist[u] < dist[v]: 
# 						dist[v] = pCrawl[1] + dist[u] 
  
# 						# update distance value  
# 						# in min heap also 
# 						minHeap.decreaseKey(v, dist[v]) 
  
# 		printArr(dist,V) 

# #4a
# # graph = Graph([
# #     ("4", "5", 0.35),  ("5", "4", -0.66),  ("4", "7", 0.37), ("5", "7", 0.28),
# #     ("7", "5", 0.28), ("5", "1", 0.32), ("0", "4", 0.38),  ("0", "2", 0.26),
# #     ("7", "3", 0.39), ("1", "3", 0.29), ("2", "7", 0.34), ("6", "2", -1.20), ("3", "6", 0.52), ("6", "0", -1.40), ("6", "4", -1.25)])
  
  
# # Driver program to test the above functions 
# graph = Graph(8) 
# graph.addEdge(4, 5, 35) 
# graph.addEdge(5, 4, -66) 
# graph.addEdge(4, 7, 37) 
# graph.addEdge(5, 7, 28) 
# graph.addEdge(7, 5, 28) 
# graph.addEdge(5, 1, 32) 
# graph.addEdge(0, 4, 38) 
# graph.addEdge(0, 2, 26) 
# graph.addEdge(7, 3, 39) 
# graph.addEdge(1, 3, 29) 
# graph.addEdge(2, 7, 34) 
# graph.addEdge(6, 2, -120) 
# graph.addEdge(3, 6, 52) 
# graph.addEdge(6, 0, -140)
# graph.addEdge(6,4,-125) 
# graph.dijkstra(0) 


# #4b
# # #graph = Graph([
# # #    ("4", "5", 0.35),  ("5", "4", -0.66),  ("4", "7", 0.37), ("5", "7", 0.28),
# # #    ("7", "5", 0.28), ("5", "1", 0.32), ("0", "4", 0.38),  ("0", "2", 0.26),
# # #    ("7", "3", 0.39), ("1", "3", 0.29), ("2", "7", 0.34), ("6", "2", 0.40), ("3", "6", 0.52), ("6", "0", 0.58), ("6", "4", 0.93)])

# graph = Graph(8) 
# graph.addEdge(4, 5, 35) 
# graph.addEdge(5, 4, -66) 
# graph.addEdge(4, 7, 37) 
# graph.addEdge(5, 7, 28) 
# graph.addEdge(7, 5, 28) 
# graph.addEdge(5, 1, 32) 
# graph.addEdge(0, 4, 38) 
# graph.addEdge(0, 2, 26) 
# graph.addEdge(7, 3, 39) 
# graph.addEdge(1, 3, 29) 
# graph.addEdge(2, 7, 34) 
# graph.addEdge(6, 2, -120) 
# graph.addEdge(3, 6, 52) 
# graph.addEdge(6, 0, -140)
# graph.addEdge(6,4,-125) 
# graph.dijkstra(0) 

# class Graph:
# 	def __init__(self):
# 		self.nodes = set()
# 		self.edges = defaultdict(list)
# 		self.distances = {}

# 	def add_node(self, value):
# 		self.nodes.add(value)

# 	def add_edge(self, from_node, to_node, distance):
# 		self.edges[from_node].append(to_node)
# 		self.edges[to_node].append(from_node)
# 		self.distances[(from_node, to_node)] = distance


# def dijsktra(graph, initial):
# 	visited = {initial: 0}
# 	path = {}

# 	nodes = set(graph.nodes)

# 	while nodes: 
# 		min_node = None
# 		for node in nodes:
# 			if node in visited:
# 				if min_node is None:
# 					min_node = node
# 				elif visited[node] < visited[min_node]:
# 					min_node = node

# 		if min_node is None:
# 			break

# 		nodes.remove(min_node)
# 		current_weight = visited[min_node]

# 		for edge in graph.edges[min_node]:
# 			weight = current_weight + graph.distances[(min_node, edge)]
# 			if edge not in visited or weight < visited[edge]:
# 				visited[edge] = weight
# 				path[edge] = min_node

# 		return visited, path

from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
	g = defaultdict(list)
	for l,r,c in edges:
		g[l].append((c,r))

	q, seen, mins = [(0,f,())], set(), {f: 0}
	while q:
		(cost,v1,path) = heappop(q)
		if v1 not in seen:
			seen.add(v1)
			path = (v1, path)
			if v1 == t: return (cost, path)

			for c, v2 in g.get(v1, ()):
				if v2 in seen: continue
				prev = mins.get(v2, None)
				next = cost + c
				if prev is None or next < prev:
					mins[v2] = next
					heappush(q, (next, v2, path))

	return float("inf")

b = [
	(4, 5, 0.35),
	(5, 4, -0.66),
	(4, 7, 0.37),
	(5, 7, 0.28),
	(7, 5, 0.28),
	(5, 1, 0.32),
	(0, 4, 0.38),
	(0, 2, 0.26),
	(7, 3, 0.39),
	(1, 3, 0.29),
	(2, 7, 0.34),
	(6, 2, 0.40),
	(3, 6, 0.52),
	(6, 0, 0.58),
	(6, 4, 0.93)
	]

a = [
	(4, 5, 0.35),
	(5, 4, 0.35),
	(4, 7, 0.37),
	(5, 7, 0.28),
	(7, 5, 0.28),
	(5, 1, 0.32),
	(0, 4, 0.38),
	(0, 2, 0.26),
	(7, 3, 0.39),
	(1, 3, 0.29),
	(2, 7, 0.34),
	(6, 2, -1.20),
	(3, 6, 0.52),
	(6, 0, -1.40),
	(6, 4, -1.25)
	]


#graph 4a
print ("4A")
print(dijkstra(a, 0, 0))
print(dijkstra(a, 0, 1))
print(dijkstra(a, 0, 2))
print(dijkstra(a, 0, 3))
print(dijkstra(a, 0, 4))
print(dijkstra(a, 0, 5))
print(dijkstra(a, 0, 6))
print(dijkstra(a, 0, 7))

graph_4a = [
	(4, 5, 0.35),
	(5, 4, 0.35),
	(4, 7, 0.37),
	(5, 7, 0.28),
	(7, 5, 0.28),
	(5, 1, 0.32),
	(0, 4, 0.38),
	(0, 2, 0.26),
	(7, 3, 0.39),
	(1, 3, 0.29),
	(2, 7, 0.34),
	(6, 2, -1.20),
	(3, 6, 0.52),
	(6, 0, -1.40),
	(6, 4, -1.25)
	]

#graph 4B
print('4B')
print(dijkstra(b, 0, 0))
print(dijkstra(b, 0, 1))
print(dijkstra(b, 0, 2))
print(dijkstra(b, 0, 3))
print(dijkstra(b, 0, 4))
print(dijkstra(b, 0, 5))
print(dijkstra(b, 0, 6))
print(dijkstra(b, 0, 7))

	# print "=== Dijkstra ==="
	# print edges
	# print "A -> E:"
	# print dijkstra(edges, "A", "E")
	# print "F -> G:"
	# print dijkstra(edges, "F", "G")


