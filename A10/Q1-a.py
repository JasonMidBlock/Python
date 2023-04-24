# 11027241 楊昀祖(Jason)

import graph
    
def findShortestPath(graph, start, end, path=[], index=1):
    #print("{0:3}: {1:5}--> {2:5}".format(index,start,end))
    nextIndex = index+1
    
    # append the start node to the path passed into this function.
    path = path + [start]
    # print('\t', path)

    #
    # case 1: the end node is reached.
    #
    if start == end:
        return path, nextIndex

    # catch the error that the start node is not in the graph.
    if not (start in graph):
        return None, None

    #
    # case 2: the end node is not reached yet.
    #
    shortestPath = None
    # for each neighoring node of the start node
    for node in graph[start]:
        # only consider those nodes not on the path to prevent looping
        if node not in path:
            # find a shortest path from a neighoring node to the end node
            newpath, newIndex = findShortestPath(graph, node, end, path, nextIndex)
            nextIndex = newIndex
            # when findShortestPath() can find a successful path
            if newpath:
                # update the shortest path when
                # (1) it is the first shortest path found or
                # (2) the subsequent path found is shorter than the current one.
                if not shortestPath or len(newpath) < len(shortestPath):
                    
                    shortestPath = newpath

    # The result for case 2 is that shortestPath contains a shortest path from the
    # start node to the end node.
    # However, it is possible that shortestpath is None if no path is found.
    #print(shortestPath)
    return shortestPath, nextIndex


G ={'EEEE': ['WEWE'], 'EEEW': ['WEWW', 'WWEW'], 'EEWE': ['WEWE', 'WWWE', 'WEWW'], \
    'EWEE': ['WWEW', 'WWWE'], 'EWEW': ['WWEW', 'WWWW'], 'WEWE': ['EEEE', 'EEWE'], \
    'WEWW': ['EEEW', 'EEWE'], 'WWEW': ['EWEE', 'EWEW', 'EEEW'], 'WWWE': ['EEWE', 'EWEE'], \
    'WWWW': ['EWEW']}


for node in G :
    path, nextIndex = findShortestPath(G,"EEEE",node )
    print("EEEE --> " + node, end=': ')
    print(nextIndex-1)
