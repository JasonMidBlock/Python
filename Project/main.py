# 11027241 楊昀祖(Jason)

from graph import *
def genStates():
    '''
    creat a all passble set 
    must including the boat 
    because there only one boat, that can judge the mover if stay with the boat
    '''
    all = []
    for man in ['E','W'] :
        for ape in ['E','W'] :
            for bull in ['E','W'] :
                for rhino in ['E','W'] :
                    for goat in ['E','W'] :
                        for cabbage in ['E','W'] :
                            for boat in ['E','W'] :
                                all.append(man+ape+bull+rhino+goat+cabbage+boat)
    return set(all)

def isAStateLegal(state):
    '''
    judge if this state is legal
    '''
    ape_with_bull = True
    ape_with_goat = True
    bull_with_rhino = True
    goat_with_cabbage = True
    if state[0] != state[1] and state[1] == state[2] :
        '''
        ape and bull stay in same side and 
        man not stay with ape and bull

        the condition is Fasle so this state is not legal
        '''
        ape_with_bull = False
    if state[0] != state[1] and state[1] == state[4] :
        '''
        ape and goat stay in same side and 
        man not stay with ape and goat

        the condition is False so this state is not legal
        '''
        ape_with_goat = False
    if state[0] != state[2] and state[2] == state[3] :
        '''
        bull and rhino stay in same side and 
        man not stay with bull and rhino
        
        the condition is Fasle so this state is not legal
        '''
        bull_with_rhino = False
    if state[0] != state[4] and state[4] == state[5] :
        '''
        goat and cabbage stay in same side and 
        man not stay with goat and cabbage

        the condition is Fasle so this state is not legal
        '''
        goat_with_cabbage = False

    if ape_with_bull and ape_with_goat and bull_with_rhino and goat_with_cabbage :
        '''
        only all the condition is ture 
        then return true
        the other states is illgal
        '''
        return True


    return False


def isNeighbor(state1,state2):
    '''
    Judge state1 and state2 two node if connect
    '''
    # just one boat
    mover = 0
    if state1[0] != state2[0] :
        #man on boat
        mover = mover + 1
    if state1[1] != state2[1] :
        #ape on boat
        mover = mover + 1
    if mover == 2 and state1[2] == state2[2] and state1[3] == state2[3] and state1[4] == state2[4] and state1[5] == state2[5]:
        # only man and ape on the boat
        # the boat is full
        return True
        
    if mover == 0 :     #no mover  
        return False

    
    if state1[0] != state2[0] and state1[0] == state1[6] and state1[6] != state2[6]:
        # first the man stay with boat
        # And both of them move to the other side
        if state1[0] == state1[1] and state1[1] != state2[1] and state1[2] == state2[2] and state1[3] == state2[3] and state1[4] == state2[4] and state1[5] == state2[5] :
            # man takes ape
            return True 
        if state1[0] == state1[2] and state1[2] != state2[2] and state1[1] == state2[1] and state1[3] == state2[3] and state1[4] == state2[4] and state1[5] == state2[5] :
            # man takes bull
            return True 
        if state1[0] == state1[3] and state1[3] != state2[3] and state1[1] == state2[1] and state1[2] == state2[2] and state1[4] == state2[4] and state1[5] == state2[5] :
            # man takes rhino
            return True 
        if state1[0] == state1[4] and state1[4] != state2[4] and state1[1] == state2[1] and state1[2] == state2[2] and state1[3] == state2[3] and state1[5] == state2[5] :
            # man takes goat
            return True 
        if state1[0] == state1[5] and state1[5] != state2[5] and state1[1] == state2[1] and state1[2] == state2[2] and state1[3] == state2[3] and state1[4] == state2[4] :
            # man takes cabbage
            return True 
        if state1[1] == state2[1] and state1[2] == state2[2] and state1[3] == state2[3] and state1[4] == state2[4] and state1[5] == state2[5] :
            # man takes only himself
            return True

    if state1[1] != state2[1] and state1[1] == state1[6] and state1[6] != state2[6]:
        if state1[1] == state1[0] and state1[0] != state2[0] and state1[2] == state2[2] and state1[3] == state2[3] and state1[4] == state2[4] and state1[5] == state2[5] :
            # man takes ape
            return True
        if state1[1] == state1[2] and state1[2] != state2[2] and state1[0] == state2[0] and state1[3] == state2[3] and state1[4] == state2[4] and state1[5] == state2[5] :
            # ape takes bull
            return True 
        if state1[1] == state1[3] and state1[3] != state2[3] and state1[0] == state2[0] and state1[2] == state2[2] and state1[4] == state2[4] and state1[5] == state2[5] :
            # ape takes rhino
            return True 
        if state1[1] == state1[4] and state1[4] != state2[4] and state1[0] == state2[0] and state1[2] == state2[2] and state1[3] == state2[3] and state1[5] == state2[5] :
            # ape takes goat
            return True 
        if state1[1] == state1[5] and state1[5] != state2[5] and state1[0] == state2[0] and state1[2] == state2[2] and state1[3] == state2[3] and state1[4] == state2[4] :
            # ape takes cabbage
            return True 
        if state1[0] == state2[0] and state1[2] == state2[2] and state1[3] == state2[3] and state1[4] == state2[4] and state1[5] == state2[5] :
            # ape takes onlt itself
            return True

    return False

def genGraph(S):
    '''
    creat a graph and return it
    '''
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



def findShortestPath(graph, start, end, path=[]):
    '''
    it use recursive concept to find the shortestpath 
    from start node to end of the input graph
    and return the path
    '''
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

def Print(Path) :
    '''
    To print the path
    '''
    man = False
    # it purpose is to mark the man is or not on boat
    for i in range(len(Path)-1):
        print(i+1, end= '. ')
        if Path[i][0] != Path[i+1][0] :
            man = True
            print('The man takes ', end  = '' )


        elif Path[i][1] != Path[i+1][1] :
            print( 'The ape takes ', end  = '' )


        if Path[i][1] != Path[i+1][1] and man:
            # the man on boat and takes ape to the other side
            print( 'the ape from ',end = '' )


        elif Path[i][2] != Path[i+1][2] :
            print('the bull from ', end = '')
        elif Path[i][3] != Path[i+1][3] :
            print('the rhino from ', end = '')
        elif Path[i][4] != Path[i+1][4] :
            print('the goat from ', end = '')
        elif Path[i][5] != Path[i+1][5] :
            print('the cabbage from ', end = '')
        else :
            # only boat and mover to the other side
            print('only itself from ', end='')

        if Path[i][6] == 'E' and Path[i+1][6] == 'W':
            print('the east to the west.')
        else:
            print('the west to the east.')
        # init if man is the mover or not 
        man = False

def main():
    setAllStates = genStates()
    G = genGraph(setAllStates)
    shortpath = findShortestPath(G, 'EEEEEEE', 'WWWWWWW')
    Print(shortpath)

main()