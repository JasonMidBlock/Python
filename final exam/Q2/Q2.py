from matplotlib.colors import TwoSlopeNorm
from graph import *
from newRiverRiddle import genStates, genGraph
from myqueue import *
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

def bfsTree(graph, node):
    """
    A function to generate a backward BFS tree from a graph with node as the root
    Input: A graph and a starting node for the search
    Output: Return a backward BFS tree rooted at node
    """
    one, two = 0, 0
    aQueue = []           # Initialize a queue
    enqueue(aQueue,node)  # enqueue node
    one = one + 1
    visited = {node}      # a set of visited nodes.
    bfsTree = {node:node} # A dictionary for the BFS tree
                          # - Key: a node n
                          # - Value: n's parent node
                          # For the root, its parent is itself.
    while aQueue:
        s = dequeue(aQueue)
        for neighbour in graph[s]:
            two = two + 1
            if neighbour not in visited:
                visited.add(neighbour)
                enqueue(aQueue,neighbour)
                one = one + 1
                bfsTree[neighbour] = s

    return one , two


one, two = bfsTree(G, 'EEEEEE')
print('The number of enqueue() functions calls: ',end ='')
print(one)

print('The number of if-condition checking: ', end='')
print(two)