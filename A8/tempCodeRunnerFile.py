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
    