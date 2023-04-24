def bfsTree(graph, node):
    """
    A function to generate a backward BFS tree from a graph with node as the root
    Input: A graph and a starting node for the search
    Output: Return a backward BFS tree rooted at node
    """
    
    aQueue = []           # Initialize a queue
    enqueue(aQueue,node)  # enqueue node
    visited = {node}      # a set of visited nodes.
    bfsTree = {node:node} # A dictionary for the BFS tree
                          # - Key: a node n
                          # - Value: n's parent node
                          # For the root, its parent is itself.
    while aQueue:
        s = dequeue(aQueue)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                enqueue(aQueue,neighbour)
                bfsTree[neighbour] = s

    return bfsTree