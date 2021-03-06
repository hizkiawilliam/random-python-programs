import time
import random
import collections
'''
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start,end="")
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3']),
         '5': set(['1', '4'])}      
'''
# Python program to print DFS traversal from a 
# given given graph 
from collections import defaultdict 
import time

start = time.time()
  
# This class represents a directed graph using 
# adjacency list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v)

    def printGraph(self): 
        print(self.graph) 
  
    # A function used by DFS 
    def DFSUtil(self,v,visited): 
  
        # Mark the current node as visited and print it 
        visited[v]= True
        print (v, end = " ") 
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self,v): 
  
        # Mark all the vertices as not visited 
        visited = [False]*(len(self.graph)) 
  
        # Call the recursive helper function to print 
        # DFS traversal 
        self.DFSUtil(v,visited) 
  
  
# Driver code 
# Create a graph given in the above diagram 

g = Graph()

g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
g.addEdge(2, 4)
g.addEdge(4, 5)
g.addEdge(5, 5)


#for i in range(0,100):
    #g.addEdge(i, i+1)

g.printGraph()    
start = time.time()
print ("Following is DFS from starting from vertex 2")
g.DFS(2)  
end = time.time()
print("")
print(end - start)

