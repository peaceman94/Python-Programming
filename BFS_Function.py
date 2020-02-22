from collections import deque

def BFS(graph, s):
  visited = set([s])
  queue = deque([s])
  
  #parent and distance dictionaries
  parent    = {s:None} 
  distance  = {s:0} 
  
  while queue:
    u = queue.popleft()
    print(u, end = " ")
    for v in graph[u]:
      if(v not in visited):
        parent[v] = u
        distance[v] = distance[u] + 1
        visited.add(v)
        queue.append(v)
  return parent, distance
        
      
g  = {0: [1, 2],1:[2], 2:[0,3], 3: [3] }
parent, distance = BFS(g, 2);
print("\n")
print(parent)
print(distance)
