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

# pack the code into a single function

def forwardBfsTree(graph, node):
  # Input: a graph and a starting node for the BFS search
  # Output: None
  # Print out the order of the BFS search
  
  aQueue = []          # Initialize an empty queue
  enqueue(aQueue,node) # enqueue node
  visited = {node}     # a set visited nodes.

  tree = {}
  while aQueue:
    s = dequeue(aQueue)
    tree[s] = set()
    for neighbour in graph[s]:
      if neighbour not in visited:
        tree[s].add(neighbour)
        visited.add(neighbour)
        enqueue(aQueue,neighbour)
  return tree

# Test Code
tree = forwardBfsTree(graph, 'A')
for node in tree.items():
  print(node)
print()
tree = forwardBfsTree(MCGW_graph, 'EEEE')
for node in tree.items():
  print(node)

# Expected results
# A D E I B J C H F G
