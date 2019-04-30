from graph import Graph
import re 

with open('data.txt') as f:
	data = f.readlines()


num_vertices = int(data[0])
print(num_vertices)
num_edges = int(data[1])

g = Graph(num_vertices)
temp = []

for i in range (2, len(data)):
	temp = re.findall(r'\d+',data[i])
	#print(temp[0])
	#print(temp[1])
	edge_1 = int(temp[0])
	edge_2 = int(temp[1])
	#print(edge_1, edge_2)
	#g.addEdge(edge_1, edge_2)

#if g.isCyclic(): 
#    print "Graph contains cycle"
#else : 
#	print "Graph does not contain cycle "


g1 = Graph(3) 
g1.addEdge(0,1) 
g1.addEdge(1,2) 
g1.addEdge(0,2)

  
if g1.isCyclic(): 
    print "Graph contains cycle"
else : 
    print "Graph does not contain cycle"

