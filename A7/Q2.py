import graph

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
    setAllStates = graph.genStates()          # Generate a set of all possible states
                                        # Each state consists of 4 characters, each of which could be
                                        # E(ast)/W(est)
                                        # The fours characters representing
                                        # - leftmost: the location (E/W) of the man
                                        # - left-middle: the location (E/W) of the cabbage
                                        # - right-middle: the location (E/W) of the goat
                                        # - rightmost: the location (E/W) of the wolf
                        
    G = graph.genGraph(setAllStates)          # Generate a graph G from the set of states (nodes)
    
    src = "EEEE"                        # The beginning state where all four objects are on the east side
    des = "WWWW"                        # The terminating state when the problem is solved

    path = graph.findShortestPath(G,src,des)  # Generate the path by finding a shortest path from
                                        # a source node src to a destination node des
    graph.printPath(path)                     # Print the path in a reading-friendly format

    return
