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
  # Output: a backward BFS tree
  
  aQueue = []             # Initialize a queue
  enqueue(aQueue,node)    # enqueue node
  visited = {node}        # a set of visited nodes.
  aBfsTree = {node:node}  # A dictionary for the backward BFS tree
                          # - Key: a node n
                          # - Value: n's parent node
                          # For the root, its parent is itself.

  while aQueue:
    s = dequeue(aQueue)
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.add(neighbour)
        enqueue(aQueue,neighbour)
        aBfsTree[neighbour] = s

  return aBfsTree

# Test Code
tree = backwardBfsTree(graph, 'A')
for node in tree.items():
  print(node)
print()
tree = backwardBfsTree(MCGW_graph, 'EEEE')
for node in tree.items():
  print(node)
