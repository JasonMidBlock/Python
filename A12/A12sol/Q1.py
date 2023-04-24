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

def forwardBfsTree(graph, node):
  # Input: a graph and a starting node for the BFS search
  # Output: a forward BFS tree
  
  aQueue = []              # Initialize an empty queue
  enqueue(aQueue,node)
  visited = {node}         # a set of visited nodes.
  aBfsTree = {node:node}   # A dictionary for the forward BFS tree
                           # - Key: a node n
                           # - Value: a set of n's children nodes
                           # For the root, its parent is itself.

  while aQueue:
    s = dequeue(aQueue)
    aBfsTree[s] = set()

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.add(neighbour)
        enqueue(aQueue,neighbour)
        aBfsTree[s].add(neighbour)

  return aBfsTree

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
