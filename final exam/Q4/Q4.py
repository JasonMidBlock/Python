from graph import *
from myqueue import *
from newRiverRiddle import genStates, genGraph

"""
G = {'EEEEEE': ['WEWEWE'], \
     'EEEEEW': ['WEWEWW', 'WEWWEW', 'WWEWEW'], \
     'EEEEWE': ['WEWEWE', 'WEWEWW', 'WEWWWE', 'WWEWWE', 'WWWEWE'], \
     'EEEWEE': ['WEWWEW', 'WEWWWE', 'WWEWEW', 'WWEWWE'], \
     'EEEWEW': ['WEWWEW', 'WEWWWW', 'WWEWEW', 'WWEWWW', 'WWWWEW'], \
     'EEWEEE': ['WEWEWE', 'WEWEWW', 'WEWWEW', 'WEWWWE', 'WWWEWE'], \
     'EEWEEW': ['WEWEWW', 'WEWWEW', 'WEWWWW', 'WWWEWW', 'WWWWEW'], \
     'EEWEWE': ['WEWEWE', 'WEWEWW', 'WEWWWE', 'WEWWWW', 'WWWEWE', 'WWWEWW', 'WWWWWE'], \
     'EWEEEE': ['WWEWEW', 'WWEWWE', 'WWWEWE'], \
     'EWEEEW': ['WWEWEW', 'WWEWWW', 'WWWEWW', 'WWWWEW'], \
     'EWEEWE': ['WWEWWE', 'WWEWWW', 'WWWEWE', 'WWWEWW', 'WWWWWE'], \
     'EWEWEE': ['WWEWEW', 'WWEWWE', 'WWEWWW', 'WWWWEW', 'WWWWWE'], \
     'EWEWEW': ['WWEWEW', 'WWEWWW', 'WWWWEW', 'WWWWWW'], \
     'WEWEWE': ['EEEEEE', 'EEEEWE', 'EEWEEE', 'EEWEWE'], \
     'WEWEWW': ['EEEEEW', 'EEEEWE', 'EEWEEE', 'EEWEEW', 'EEWEWE'], \
     'WEWWEW': ['EEEEEW', 'EEEWEE', 'EEEWEW', 'EEWEEE', 'EEWEEW'], \
     'WEWWWE': ['EEEEWE', 'EEEWEE', 'EEWEEE', 'EEWEWE'], \
     'WEWWWW': ['EEEWEW', 'EEWEEW', 'EEWEWE'], \
     'WWEWEW': ['EEEEEW', 'EEEWEE', 'EEEWEW', 'EWEEEE', 'EWEEEW', 'EWEWEE', 'EWEWEW'], \
     'WWEWWE': ['EEEEWE', 'EEEWEE', 'EWEEEE', 'EWEEWE', 'EWEWEE'], \
     'WWEWWW': ['EEEWEW', 'EWEEEW', 'EWEEWE', 'EWEWEE', 'EWEWEW'], \
     'WWWEWE': ['EEEEWE', 'EEWEEE', 'EEWEWE', 'EWEEEE', 'EWEEWE'], \
     'WWWEWW': ['EEWEEW', 'EEWEWE', 'EWEEEW', 'EWEEWE'], \
     'WWWWEW': ['EEEWEW', 'EEWEEW', 'EWEEEW', 'EWEWEE', 'EWEWEW'], \
     'WWWWWE': ['EEWEWE', 'EWEEWE', 'EWEWEE'], \
     'WWWWWW': ['EWEWEW']}
"""

listAllStates = genStates()
G = genGraph(listAllStates)

# Write your code below
def modifiedBsfTree(graph, node):
  # Input: a graph and a starting node for the search
  # Output: a BFS "tree" rooted at node
  #         The keys are nodes.
  #         The value of a node is a set of the node's parent nodes
  #         on the backward BFS tree.



#
# (DO NOT REMOVE) Code for Rocky's testing
# setNodeRemoved is the set of the nodes removed due to the new constraint.
#
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

tree = modifiedBsfTree(G, 'EEEEEE')
for node in tree.keys():
    if node != "EEEEEE":
        print(node+":",tree[node])
print()
