from graph import *
from myqueue import *

#
# Uncomment the dictionary for the graph below ONLY WHEN you cannot generate a correct graph.
# You may use this graph to get a shortest path and print out the solution.
#
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

def solver():
    """
    A main program to print out the path that solves the puzzle.
      Input: None
      Output:
      - Return None
      - Print the solution to the riddle.
    """
    listAllStates = genStates()         # Generate a list of all possible states
                                        # Each state consists of 6 characters, each of which could be
                                        # E(ast)/W(est)
                                        # Starting from the left, the six characters are the locations of
                                        # - Albert,
                                        # - Billy,
                                        # - Cathy,
                                        # - David,
                                        # - Eliza, and
                                        # - Frank.
    
    G = genGraph(listAllStates)         # Generate a graph G from the list of states (nodes)

    src = "EEEEEE"                      # The beginning state where all six objects are on the east side
    des = "WWWWWW"                      # The terminating state when the riddle is solved

    path = findShortestPath(G,src,des)  # Generate the path by finding a shortest path from
                                        # a source node src to a destination node des
                                        
    printPath(path)                     # Print the path in a reading-friendly format
    
    #
    # (DO NOT REMOVE) This code is for facilitating Rocky's grading
    #
    print()
    print("The list of all possible states:")
    count = 0
    for node in listAllStates:
        if count % 6 == 0:
            print()
            print(str(count+1)+":\t", end=" ")
        print(node, end="    ")
        count += 1
    print()
    print()
    print("The graph:")
    count = 1
    for node in G.items():
        print(str(count)+":\t", node[0]+":",node[1])
        count += 1
    print()

    return

    
def genStates():
    """
    A function to generate a list of all possible states "E/W,E/W,E/W,E/W,E/W,E/W"
    Input: None
    Output: Return a LIST of all possible states "E/W,E/W,E/W,E/W,E/W,E/W" in a
            lexicographical order (i.e., "EEEEEE", "EEEEEW", "EEEEWE", and so on).
    """
    all = []
    for Albert in ['E','W'] :
        for Billy in ['E','W'] :
            for Catherine in ['E','W'] :
                for David in ['E','W'] :
                    for Eliza in ['E','W'] :
                        for Frank in ['E','W'] :
                                all.append(Albert+Billy+Catherine+David+Eliza+Frank)
    return set(all)



def genGraph(S):
    """
    A function to generate a graph from a list of all possible states S
    Input: S, a list of all possible states
    Output: Return a graph that abstracts the river-crossing riddle.
    """
    graph={}
    # Add legal nodes to the graph
    for state in S:
        if isAStateLegal(state) == True:    # check whether a node (state) is legal
            addNode(graph,state)
            # addNode use liberary   
            # If legal, add state in the set of all legal states
    for state in getNodes(graph):
        for otherState in getNodes(graph): # getNodes use liberary   
            if isNeighbor(state,otherState) and not isLinked(graph,state,otherState):  # isLink use liberary   
                addLink(graph,state,otherState)
                # addLink use liberary
    return graph
            
def isAStateLegal(state):
    """
    A function to determine whether a state is legal or not
    Input: A state
    Output: If a state is legal, return True; else, False
    """
    B_with_C = True
    C_with_D = True
    D_with_E = True
    E_with_F = True
    if state[0] != state[1] and state[1] == state[2] :
        B_with_C = False
    if state[0] != state[2] and state[2] == state[3] :
        C_with_D = False
    if state[0] != state[3] and state[3] == state[4] :
        D_with_E = False
    if state[0] != state[4] and state[4] == state[5] :
        E_with_F = False

    if B_with_C and C_with_D and D_with_E and E_with_F :
        return True

    return False




def isNeighbor(state1,state2):
    """
    A function to determine whether there is a link between state1 and state2
    Input: Two states, state1 and state2
    Output: Return True if there is a link between the two states; return False, otherwise.
    """
    if state1[0] == state2[0] :
        return False
    mover = 0
    # 一開始和A同邊的
    staywithA=[]
    notstaywithA=[]
    for i in range(1,6) :
        if state1[i] == state1[0] :
            staywithA.append(i)
        else :
            notstaywithA.append(i)

    # 如果有不同邊的移動   return false
    for i in notstaywithA :
        if state1[i] != state2[i] :
            return False

    for i in staywithA :
        if state1[i] != state2[i]:
            mover = mover + 1 

    if mover <= 2 :
        return True
    
    return False


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


def findShortestPath(G, src, dest):
    """
    A function generate a shortest path from a source and a destination
    Inputs:
    - G: A graph
    - src: A source node
    - dest: A destination node
    Output: Return a shortest path in the form of a list
    """

    # Return a BFS tree rooted at src
    aTree = bfsTree(G, src)
    shortestPath = [dest]        # A list for a shortest path
    node = dest
    while aTree[node] != node:   # Check whether reaching the root
        shortestPath.append(aTree[node])
        node = aTree[node]

    shortestPath.reverse()
    return shortestPath


def printPath(path):
    """
    A function to print out the solution to the riddle in a reading friendly format.
    Input: path, a shortest path
    Output:
    - Return None
    - Print out the solution in a reading-friendly format.
    """

    for i in range(len(path)-1):
        first_on_boat = False
        move_list =[0]
        if path[i][0] == 'E':
            from_site ='E'
        else :
            from_site = 'W'
        print(i+1, end ='.')
        print(' Albert takes ' ,end = '')
        if path[i][1] != path[i+1][1]:
            first_on_boat = True
            move_list.append(1)
            print( 'Billy ', end ='' )
        if path[i][2] != path[i+1][2] :
            if first_on_boat:                             #Billy+Catherine+David+Eliza+Frank
                print('and Catherine ', end ='' )
            else :
                first_on_boat = True
                print('Catherine ',end ='')
        
        if path[i][3] != path[i+1][3] :
            if first_on_boat:
                print('and David ', end ='' )
            else :
                first_on_boat = True
                print('David ',end ='')

        if path[i][4] != path[i+1][4] :
            if first_on_boat:
                print('and Eliza ', end ='' )
            else :
                first_on_boat = True
                print('Eliza ',end ='')

        if path[i][5] != path[i+1][5] :
            if first_on_boat:
                print('and Frank ', end ='' )
            else :
                first_on_boat = True
                print('Frank ',end ='')

        if first_on_boat == False :
            print('himself ', end ='')
        
        if from_site == 'E' :
            print('from the east to the west. ')
        else :
            print('from the west to the east. ')
        

# run the program
if __name__ == "__main__":
    solver()