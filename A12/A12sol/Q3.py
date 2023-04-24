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
  # Input: a graph and a starting node for the search
  # Output: None
  # Print out the order of the search
  aQueue = []              # Initialize an empty queue
  enqueue(aQueue,node)     # enqueue node
  visited = {node}         # a set of visited nodes
  aBfsTree = {node:{node}} # A dictionary for the forward BFS tree
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

def backwardBfsTree(graph, node):
  # Input: a graph and a starting node for the search
  # Output: a BFS tree rooted at node
  
  aQueue = []            # Initialize an empty queue
  enqueue(aQueue,node)   # enqueue node
  visited = {node}       # a set of visited nodes
  aBfsTree = {node:node} # A dictionary for the backward BFS tree
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

def findLeafNodesfromForwardTree(tree):
    """
    Input: A forward BFS tree
    Output: A set of leaf nodes in the BFS tree
    """
    setLeafNodes = set()
    for node in tree.keys():
        if not tree[node]:
            setLeafNodes.add(node)

    return setLeafNodes

def findLeafNodesfromBackwardTree(tree):
    """
    Input: A backward BFS tree
    Output: A set of leaf nodes in the BFS tree
    """
    setNonLeafNodes = set()
    for node in tree.values():
        setNonLeafNodes.add(node)
        
    return set(tree.keys()) - setNonLeafNodes

print("Forward tree:")
print(findLeafNodesfromForwardTree(forwardBfsTree(graph,"A")))
print(findLeafNodesfromForwardTree(forwardBfsTree(MCGW_graph,"EEEE")))
print()
print("Backward tree:")
print(findLeafNodesfromBackwardTree(backwardBfsTree(graph,"A")))
print(findLeafNodesfromBackwardTree(backwardBfsTree(MCGW_graph,"EEEE")))


        
    
