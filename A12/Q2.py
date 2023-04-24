#11027241 楊昀祖 (Jsaon)
from myqueue import *


graph = {
  'A' : ['D', 'E', 'I'],
  'B' : ['D'],
  'C' : ['E', 'H', 'J'],
  'D' : ['A', 'B', 'E', 'J'],
  'E' : ['A', 'C', 'D', 'H'],
  'F' : ['H', 'I'],
  'G' : ['H'],
  'H' : ['C', 'E', 'F', 'G'],
  'I' : ['A', 'F'],
  'J' : ['C', 'D']
}

MCGW_graph ={
  'EEEE':['WEWE'],
  'WEWE':['EEEE','EEWE'],
  'EEWE':['WEWE','WWWE','WEWW'],
  'WWWE':['EEWE','EWEE'],
  'EWEE':['WWWE','WWEW'],
  'WEWW':['EEWE','EEEW'],
  'EEEW':['WEWW','WWEW'],
  'WWEW':['EWEE','EEEW','EWEW'],
  'EWEW':['WWEW','WWWW'],
  'WWWW':['EWEW']
}

def backwardBfsTree(graph, node):
  # Input: a graph and a starting node for the BFS search
  # Output: None
  # Print out the order of the BFS search
  
  aQueue = []          # Initialize an empty queue
  enqueue(aQueue,node) # enqueue node
  visited = {node}     # a set visited nodes.

  tree = {}
  tree[node] = node
  while aQueue:
    s = dequeue(aQueue)
    for neighbour in graph[s]:
      if neighbour not in visited:
        tree[neighbour] = s
        visited.add(neighbour)
        enqueue(aQueue,neighbour)
  return tree



tree = backwardBfsTree(graph, 'A')

print(tree)
for node in tree.items():
    print(node)
print()
tree = backwardBfsTree(MCGW_graph, 'EEEE')
for node in tree.items():
    print(node)