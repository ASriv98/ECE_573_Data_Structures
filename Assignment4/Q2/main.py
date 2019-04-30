from Kruskal import Graph
import re 
import time

with open('data.txt') as f:
	data = f.readlines()


num_vertices = int(data[0])
num_edges = int(data[1])
print(num_vertices)
#print(data)
g = Graph(num_vertices)
temp = []

for i in range (2, len(data)):
	temp = re.findall(r'(\d+(?:\.\d+)?)',data[i])
	edge_1 = int(temp[0])
	edge_2 = int(temp[1])
	weight = float(temp[2])
	print(weight)
	#print(edge_1, edge_2, weight)
	g.addEdge(edge_1, edge_2, weight)

start = time.time()
g.KruskalMST()
end = time.time()

print("Kruskal time: ", end-start)

