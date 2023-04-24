from graph import *
    
def findShortestPath(graph, start, end, path=[]):
    """
    A function to find a shortest path from start to end on a graph
    This function is obtained from https://www.python.org/doc/essays/graphs/
    with one change due to the deprecation of the method has_key().
    
    Input: A graph, a starting node, an end node and an empty path
    Output: Return the shortest path in the form of a list.
    """
    
    path = path + [start]
    if start == end:
        return path
    if not (start in graph):
        return None
    shortestPath = None
    for node in graph[start]:
        if node not in path:
            newpath = findShortestPath(graph, node, end, path)
            if newpath:
                if not shortestPath or len(newpath) < len(shortestPath):
                    shortestPath = newpath
    return shortestPath


def printPath(path):
    """
    A function to print out the solution in a reading friendly format.
    Input: A shortest path
    Output: Print out the solution to the MCGW problem and return True.
    """
    
    for nodeOnPath in range(len(path)-1):
        # For each node on the path, except the last one, determine
        # the direction of crossing the river.
        if path[nodeOnPath][0] == "E":
            fromDirection = "east"
            toDirection = "west"
        else:
            fromDirection = "west"
            toDirection = "east"

        # The man takes only himself.
        whichObjectToTakeWithMan = 0
        
        # Determine whether the man takes other object with him.
        for j in range(1,4):
            if path[nodeOnPath][j] != path[nodeOnPath+1][j]:
                whichObjectToTakeWithMan = j
                break

        # Include the description of the objects to be carried by the man.
        if  whichObjectToTakeWithMan == 1:
            nameOfObject = "the cabbage"
        elif whichObjectToTakeWithMan == 2:
            nameOfObject = "the goat"
        elif whichObjectToTakeWithMan == 3:
            nameOfObject = "the wolf"
        else:
            nameOfObject = "only himself"

        # print out the objects being shipped each time by the man in order
        # to bring all three objects from the east to the west.
        print(str(nodeOnPath+1) + ". " + "The man takes " + nameOfObject + " from the " \
              + fromDirection + " to the " + toDirection + ".")

    return True    


    
G ={'EEEE': ['WEWE'], 'EEEW': ['WEWW', 'WWEW'], 'EEWE': ['WEWE', 'WWWE', 'WEWW'], \
    'EWEE': ['WWEW', 'WWWE'], 'EWEW': ['WWEW', 'WWWW'], 'WEWE': ['EEEE', 'EEWE'], \
    'WEWW': ['EEEW', 'EEWE'], 'WWEW': ['EWEE', 'EWEW', 'EEEW'], 'WWWE': ['EEWE', 'EWEE'], \
    'WWWW': ['EWEW']}

path = findShortestPath(G,"EEEE","WWWW")
printPath(path)

