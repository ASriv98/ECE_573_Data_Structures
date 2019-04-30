# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
import re
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            print (s)
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
  


with open('data.txt') as f:
    data = f.readlines()


num_vertices = int(data[0])
num_edges = int(data[1])
print(num_vertices)
#print(data)
g = Graph()
temp = []

for i in range (2, len(data)):
    temp = re.findall(r'(\d+(?:\.\d+)?)',data[i])
    edge_1 = int(temp[0])
    edge_2 = int(temp[1])
    #print(edge_1, edge_2, weight)
    g.addEdge(edge_1, edge_2)


  
# Driver code 

print "Following is BFS from (starting from vertex 2)"
g.BFS(2) 
  
# This code is contributed by Neelam Yadav 