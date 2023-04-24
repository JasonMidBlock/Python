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
        tree[neighbour] = s
        visited.add(neighbour)
        enqueue(aQueue,neighbour)
  return tree

def findLeafNodesfromForwardTree(tree) :
    list1 = []
    for two_node in tree :
      if tree[two_node] == set():
        list1.append(two_node)
    return list1

def findLeafNodesfromBackwardTree(tree):
    list1 = []
    for two_node in tree :
      list1.append(two_node)
      if tree[two_node] in list1 :
        list1.remove(tree[two_node])
    return list1


print("Forward tree:")
print(findLeafNodesfromForwardTree(forwardBfsTree(graph,"A")))
print(forwardBfsTree(graph,"A"))
print(findLeafNodesfromForwardTree(forwardBfsTree(MCGW_graph,"EEEE")))
print()

print("Backward tree:")
print(findLeafNodesfromBackwardTree(backwardBfsTree(graph,"A")))
print(findLeafNodesfromBackwardTree(backwardBfsTree(MCGW_graph,"EEEE")))
