#11027241 楊昀祖(Jason)
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
  aQueue.append(node) # enqueue node
  visited = {node}     # a set visited nodes.

  tree = {}
  while aQueue:
    s = aQueue.pop(0)
    tree[s] = set()
    for neighbour in graph[s]:
      if neighbour not in visited:
        tree[s].add(neighbour)
        visited.add(neighbour)
        aQueue.append(neighbour)
  return tree


def  findShortestPath(tree, src, dest,path=[]):
    path = path + [src]

    if src == dest:
        return path

    if not (src in tree):
        return path

    shortestPath = None
    for node in tree[src]:
        if node not in path:
            newpath = findShortestPath(tree, node, dest, path)
            if newpath:
                if not shortestPath or len(newpath) < len(shortestPath):
                    
                    shortestPath = newpath
    return shortestPath

print('For the 10-node graph:')
listgraph=[]
itemgraph = forwardBfsTree(graph, 'A')

for key in graph:
    listgraph.append(key)
startnode = listgraph[0]
for node in listgraph :
    print("{0} --> {1}: {2}".format(startnode, node,findShortestPath(graph, startnode, node)) )
print()


print('For the MCGW graph:')
listMCGW = []
itemMCGW = forwardBfsTree(MCGW_graph, 'EEEE')
for key in MCGW_graph:
    listMCGW.append(key)
startnode = listMCGW[0]
for node in itemMCGW :
    print("{0} --> {1}: {2}".format(startnode, node , findShortestPath(MCGW_graph, startnode, node)))