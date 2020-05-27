import time
import psutil

# Python program to print DFS traversal from a 
# given given graph 
from collections import defaultdict 
import time
  
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
        #print (v, end = " ") 
  
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

'''
g.addEdge(5, 7) 
g.addEdge(7, 7)
g.addEdge(6, 8)
g.addEdge(8, 9)
g.addEdge(9, 9)
g.addEdge(9, 10)
g.addEdge(10, 11)

g.addEdge(9, 11) 
g.addEdge(11, 11)
g.addEdge(10, 12)
g.addEdge(12, 13)
g.addEdge(12, 14)
g.addEdge(13, 14)
g.addEdge(14, 14)
g.addEdge(15, 15)

g.addEdge(14, 16) 
g.addEdge(16, 16)
g.addEdge(15, 17)
g.addEdge(17, 18)
g.addEdge(17, 19)
g.addEdge(18, 19)
g.addEdge(19, 19)
g.addEdge(20, 20)
'''

g.printGraph()    
print ("Following is DFS from starting from vertex 2")
start = time.time()
g.DFS(2)
print(float(psutil.cpu_percent()))
dict_ram = (dict(psutil.virtual_memory()._asdict()))
end = time.time()
print("Running time: ",end - start)

