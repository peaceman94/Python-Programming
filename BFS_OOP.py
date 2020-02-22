# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:25:14 2020

@author: Shivam
"""

from collections import defaultdict

# Define the class object graph which stores the graph in adjacency list format
class Graph:
  
  def __init__(self):
    """
    Initialize the graph with default dict
    """
    self.graph    = defaultdict(list)

  def add_edge(self, u, v):
    self.graph[u].append(v)

# define BFS as object
class BFS(Graph):
  
  def __init__(self, source=None):
    super().__init__()
    self.initialize_BFS_settings(source)
    self.BFS_Ran = False;
  
  def initialize_BFS_settings(self, source):
    self.distance = defaultdict(lambda: float('inf') )
    self.parent   = defaultdict(lambda: None)
    self.visited  = defaultdict(bool)
    self.source   = source

  def add_parent(self, parent, child):
    self.parent[child] = parent
  
  def update_distance(self, vertex, distance):
    self.distance[vertex] = distance
  
  def print_shortest_path(self, v):
    if(not self.BFS_Ran):
      print('BFS routine not run. Hence distances and parents not calculated. Please run BFS and rerun')
      return
    
    if(not self.visited[v]):
      print("vertex {} not reachable from vertex {}".format(v, self.source) )
      return
    
    print('printing path to reach {} (source is {}):'.format(v, self.source))
    print(v, end = ' ')
    while( self.parent[v] != None):
      print('<---', self.parent[v], end = " ")
      v = self.parent[v]
    return
 
  
  def Run(self, s):
    """
    Every time the BFS routine is run, update the distance, visited and parent dictionary
    """
    self.initialize_BFS_settings(s)
    self.BFS_Ran = True
    #create Queue
    q = []
    
    #update the source distance and add it to q
    self.update_distance(s, 0)
    self.visited[s] = True
    q.append(s)
    
    while q:
      u = q.pop(0)
      print (u, end = "\n") 
      for v in self.graph[u]:
        if(self.visited[v] == False):
          self.update_distance(v, self.distance[u]+1)
          self.add_parent(u, v)
          q.append(v)
          self.visited[v] = True

#run the above
g = BFS();
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 

g.Run(3)
#print(g.distance)

g.print_shortest_path(1)
#print(g.graph)
