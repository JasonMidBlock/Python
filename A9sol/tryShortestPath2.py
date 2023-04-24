from graph import *
    
def findShortestPath(graph, start, end, path=[]):
    """
    A function to find a shortest path from start to end on a graph
    This function is obtained from https://www.python.org/doc/essays/graphs/
    with one change due to the deprecation of the method has_key().
    
    Input: A graph, a starting node, an end node and an empty path
    Output: Return
    - A shortest path in the form of a list and
    - The total number of recursive function calls, including this one
    """
    
    # append the start node to the path passed into this function.
    path = path + [start]

    #
    # case 1: the end node is reached.
    #
    if start == end:
        return path, 1

    # catch the error that the start node is not in the graph.
    if not (start in graph):
        return None, None

    #
    # case 2: the end node is not reached yet.
    #
    shortestPath = None
    totalNum = 0
    # for each neighoring node of the start node
    for node in graph[start]:
        # only consider those nodes not on the path to prevent looping
        if node not in path:
            # find a shortest path from a neighoring node to the end node
            newpath, num = findShortestPath(graph, node, end, path)
            # when findShortestPath() can find a successful path
            if newpath:
                # update the shortest path when
                # (1) it is the first shortest path found or
                # (2) the subsequent path found is shorter than the current one.
                if not shortestPath or len(newpath) < len(shortestPath):
                    shortestPath = newpath
            totalNum += num

    # The result for case 2 is that shortestPath contains a shortest path from the
    # start node to the end node.
    # However, it is possible that shortestpath is None if no path is found.
    return shortestPath, totalNum+1


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

path, totalCall = findShortestPath(G,"EEEE","WWWW")
printPath(path)
print()
print("The total number of recursive function calls is:", totalCall)

