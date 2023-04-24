from graph import *

def solver():
    """
    The main program to print out the path that solves the problem.
    Input: None
    Output:
      - Return none
      - Print out a solution to the MCGW problem
          1. The man takes the goat from the east to the west.
          2. The man takes only himself from the west to the east.
          3. The man takes the wolf from the east to the west.
          4. The man takes the goat from the west to the east.
          5. The man takes the cabbage from the east to the west.
          6. The man takes only himself from the west to the east.
          7. The man takes the goat from the east to the west.
    """
    setAllStates = genStates()          # Generate a set of all possible states
                                        # Each state consists of 4 characters, each of which could be
                                        # E(ast)/W(est)
                                        # The fours characters representing
                                        # - leftmost: the location (E/W) of the man
                                        # - left-middle: the location (E/W) of the cabbage
                                        # - right-middle: the location (E/W) of the goat
                                        # - rightmost: the location (E/W) of the wolf
                        
    G = genGraph(setAllStates)          # Generate a graph G from the set of states (nodes)
    
    src = "EEEE"                        # The beginning state where all four objects are on the east side
    des = "WWWW"                        # The terminating state when the problem is solved

    path = findShortestPath(G,src,des)  # Generate the path by finding a shortest path from
                                        # a source node src to a destination node des
    printPath(path)                     # Print the path in a reading-friendly format

    return

    
def genStates():
    """
    A function to generate a set of all possible states (E/W,E/W,E/W,E/W)
    Input: None
    Output: Return a set of all possible states (E/W,E/W,E/W,E/W).
    """

    direction = ("E","W")
    states = []
    for i in direction:
        for j in direction:
            for k in direction:
                for l in direction:
                    aState = i + j + k + l  # Concatenate the four locations into a string
                    states.append(aState)   # Add the newly created state to the set of states

    return set(states)


def genGraph(S):
    """
    A function to generate a graph from a set of all possible states S
    Input: A set of all possible states
    Output: Return a graph based on a set of all possible states and given constraints
    """
    
    # Create an empty dictionary for the final graph
    MCGWgraph={}

    # Add legal nodes to the graph
    for state in S:
        if isAStateLegal(state) == True:     # check whether a node (state) is legal
            addNode(MCGWgraph,state)         # If legal, add n to the set of all legal states <------

    for state in getNodes(MCGWgraph):
        for otherState in getNodes(MCGWgraph):
            if isNeighbor(state,otherState) and not isLinked(MCGWgraph,state,otherState):
                addLink(MCGWgraph,state,otherState)
        
    return MCGWgraph

            
def isAStateLegal(state):
    """
    A function to determine whether a state is legal or not
    Input: A state
    Output: If a state is legal, return true; else, false
    """


def isNeighbor(state1,state2):
    """
    A function to determine whether two states are neighboring to each other
    Input: Two states, state1 and state2
    Output: Return true if they are neighbors; return false, otherwise.
    """
    

# You are not expected to implement this function.
# You should have the skill of finding a suitable implementation
# to help solve the program.
def findShortestPath(graph, start, end, path=[]):
    """
    A function to find a shortest path from start to end on a graph
    This function is obtained from https://www.python.org/doc/essays/graphs/
    with one change due to the deprecation of the method has_key().
    
    Input: A graph, a starting node, an end node and an empty path
    Output: Return a shortest path in the form of a list.
    """
    
    path = path + [start]
    if start == end:
        return path
#    if not graph.has_key(start):
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
    Input: A sequence of states that is a solution to the MCGW problem
    Output:
      - Print out the solution to the MCGW problem stated in the docstring
        in solver().
      - Return none
    """



# run the program
solver()
