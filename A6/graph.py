"""
This library provides a number of methods for manipulating a graph.
"""

def getNodalDeg(G,n):
    """
    Input: G, a graph and n, a node in G
    Output: Return the nodal degree of n
    """
    return len(G[n])
    
def getNodes(G):
    """
    Input: G, a graph
    Output: Return the set of nodes in G
    """
    return set(G.keys())
    
def getLinks(G):
    """
    Input: G, a graph
    Output: Return the set of links in G
            Each link is implemented as a tuple (a,b), where
            the link starts from node a and ends at node b.
    """
    setLinks = set()
    for i,j in G.items():
        for k in j:
            setLinks.add((i,k))

    return setLinks

def getNeighbors(G,n):
    """
    Input: G, a graph and n, a node in G
    Output: Return a set of nodes in G to which n is connected.
    """
    return G[n]

def isLinked(G, n1, n2):
    """
    Input: G, a graph and n1 and n2, two different nodes in G
    Output: Return True if there is a link between n1 and n2; False, otherwise
    """
    return n2 in G[n1]

def addNode(G, n):
    """
    Input:
      - G: An existing graph
      - n: A node which may or may not be in G.
    Output:
      - If n is already in G, return True.
      - Else, G will be updated by including n and return True.
    """
    if n not in G:
        G[n] = set()
    
    return True

def addLink(G, n1, n2):
    """
    Input:
      - G: An existing graph
      - Two nodes n1 and n2 which may or may not be in G.
    Output:
      - If n1 or n2 is not in G, add the node(s) to G.
      - G will be updated by including a undirected link (n1,n2)
      - Return True
    """
    if n1 not in G:
        addNode(G, n1)
    if n2 not in G:
        addNode(G, n2)
    G[n1].add(n2)
    G[n2].add(n1)
    
    return True

def delNode(G, n):
    """
    Input:
      - G: An existing graph
      - n: A node which may or may not be in G.
    Output:
      - If n is in G, G will be updated by removing n and its links and return True.
      - Else, print an error message and return False.
    """
    if n not in G:
        print("Error: The node is not in the graph.")
        return False

    for node in G[n]:
        G[node].remove(n)
    del G[n]
    
    return True

def delLink(G, n1, n2):
    """
    Input:
      - G: An existing graph
      - n1 and n2: two existing nodes in G
    Output:
      - If n1 and n2 are in G, G will be updated with the undirected link
        (n1,n2) removed from G. Return True.
      - Otherwise, print an error message and return False.
    """
    if n1 not in G or n2 not in G:
        print("Error: Not both nodes are in the graph.")
        return False

    G[n1].remove(n2)
    G[n2].remove(n1)

    return True

