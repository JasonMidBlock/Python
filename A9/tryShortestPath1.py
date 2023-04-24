def findShortestPath(graph, start, end, path=[]):    
    path = path + [start]
    #add one site in passed site recode
    if start == end:
        #when path in the end and return the passed recode
        return path
    
    if not (start in graph):
        #if the start Node is illegal
        return None

    shortestPath = None

    for node in graph[start] : 
        if node not in path :
            # if node is not passed and add in path
            newpath = findShortestPath(graph, node, end, path) 
            # find the next path
            if newpath:     # newpath not none
                if not shortestPath or len(newpath) < len(shortestPath):
                    # if shortestPath not None let shortestPath init
                    shortestPath = newpath
    return shortestPath
