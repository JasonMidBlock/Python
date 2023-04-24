import graph
#print(graph.__doc__)

print()
fileName = input("Please input a text file for a graph: ")
infile = open(fileName,encoding="utf8")
aGraph = dict()
     
for line in infile:
    linesplit = line.split()
    graph.addLink(aGraph, linesplit[0], linesplit[1])

print("(A) A dictionary implementation of the graph. Key: String; value: A set of strings:")
print(aGraph)
print()

print("(B) The nodal degrees:")
for i in aGraph.keys():
    print("Node "+i+": ", graph.getNodalDeg(aGraph,i))
print()

print("(C) The set of nodes:")
print(graph.getNodes(aGraph))

print("The number of nodes is", str(len(graph.getNodes(aGraph)))+".")
print()

print("(D) The set of links:")
print(graph.getLinks(aGraph))

print("The number of unidirected links is", str(int(len(graph.getLinks(aGraph))/2))+".")
print()

print("(E) The neighbors of the nodes:")
for i in aGraph.keys():
    print(i+':', graph.getNeighbors(aGraph,i))
print()

print("(F) Testing connectivity:")
print("B is connected to A:", graph.isLinked(aGraph, "B", "A"))
print("G is connected to A:", graph.isLinked(aGraph, "G", "A"))
print()

print("(G) Deleting nodes:")
print("Case 1: Deleting node 'Z'")
graph.delNode(aGraph, "Z")
print("Case 2: Deleting node 'C'")
graph.delNode(aGraph, "C")
print(aGraph)
print()

print("(H) Deleting links:")
print("Case 1: Deleting link C--A")
graph.delLink(aGraph, "C", "A")
print("Case 2: Deleting link E--G")
graph.delLink(aGraph, "E", "G")
print(aGraph)
print("Case 3: Deleting link F--B")
graph.delLink(aGraph, "F", "B")
print(aGraph)
print()
