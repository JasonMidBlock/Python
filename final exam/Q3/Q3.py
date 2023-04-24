from graph import *
from newRiverRiddle import genStates, genGraph, bfsTree

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

listAllStates = genStates()
G = genGraph(listAllStates)

# Write your code below


#
# (DO NOT REMOVE) Code for Rocky's testing
# setNodeRemoved is the set of the nodes removed due to the new constraint.
#


setNodeRemoved = set()
for i in list(G.keys) :
    if i == 'WWEWWW' or 'EEWEEE' or 'WWWWEW' or 'WWWWEW' :
        setNodeRemoved.add(i)
        delNode(G, i)
    else :
        for node in i :
            if i == 'WWEWWW' or 'EEWEEE' or 'WWWWEW' or 'WWWWEW' :
                setNodeRemoved.add(node)
                delLink(G, i, node)

print("The nodes removed are:", setNodeRemoved)
print()

print("The graph:")
count = 1
for node in G.items():
    print(str(count)+":\t", node[0]+":",node[1])
    count += 1
print()

print("The backward tree:")
tree = bfsTree(G, 'EEEEEE')
for node in tree.keys():
    print(node+":",tree[node])
