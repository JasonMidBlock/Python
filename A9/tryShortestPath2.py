# 11027241 楊昀祖(Jason)

from itertools import count
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

    src = 'EEEE'                        # The beginning state where all four objects are on the east side
    des = 'WWWW'                        # The terminating state when the problem is solved
    path, time = findShortestPath(G,src,des)  # Generate the path by finding a shortest path from
                                        # a source node src to a destination node des
    print("The sequence of recursive function calls : ")
    printPath(path)                     # Print the path in a reading-friendly format
    print()
    print("This number of recursive function is: ", time)
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
    if state[1] != state[2] and state[2] != state[3] :
        return True
    elif state[1] == state[2] and state[0] == state[1] :
        return True
    elif state[2] == state[3] and state[0] == state[2] :
        return True
    return False


def isNeighbor(state1,state2):
    if state1[0] == state2[0] :
        return False
    elif state1[1] != state2[1] and state1[2] != state2[2] :
        return False
    elif state1[2] != state2[2] and state1[3] != state2[3] :
        return False
    elif state1[1] != state2[1] and state1[3] != state2[3] :
        return False
    else :
        return True

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
    time =1

    path = path + [start]
    if start == end:
        return path, time
    if not (start in graph):
        return None, time
    shortestPath = None
    for node in graph[start]:
        if node not in path:
            newpath, count = findShortestPath(graph, node, end, path)
            time += count
            if newpath:
                # if newpath is not none
                if not shortestPath or len(newpath) < len(shortestPath) :
                    shortestPath = newpath
    return shortestPath, time

def printPath(path) :
    """
    A function to print out the solution in a reading friendly format.
    Input: A sequence of states that is a solution to the MCGW problem
    Output:
      - Print out the solution to the MCGW problem stated in the docstring
        in solver().
      - Return none
    """
    for i in range(len(path)-1):
        print(i+1, end = '. ')
        print('The man takes ', end='')
        if path[i][1] != path[i+1][1] :
            if path[i][0] == 'E' :
                print('the wolf from the east to the west.')
            else :
                print('the wolf from the west to the east.')
        elif path[i][2] != path[i+1][2] :
            if path[i][0] == 'E' :
                print('the goat from the east to the west.')
            else :
                print('the goat from the west to the east.')
        elif path[i][3] != path[i+1][3] :
            if path[i][0] == 'E' :
                print('the cabbage from the east to the west.')
            else :
                print('the cabbage from the west to the east.')    
        else :
            if path[i][0] == 'E' :
                print('the only himself from the east to the west.')
            else :
                print('the only himself the west to the east.') 

# run the program
solver()
