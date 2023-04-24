#11027241 楊昀祖(Jason)
G = {
  'A' : ['D', 'E', 'I'],
  'B' : ['D'],
  'C' : ['E', 'H', 'J'],
  'D' : ['A', 'B', 'E', 'J'],
  'E' : ['A', 'C', 'D', 'H'],
  'F' : ['H', 'I'],
  'G' : ['H'],
  'H' : ['C', 'E', 'F', 'G'],
  'I' : ['A', 'F'],
  'J' : ['C', 'D']
}

MCGW_G ={
"EEEE":["WEWE"],
"WEWE":["EEEE","EEWE"],
"EEWE":["WEWE","WWWE","WEWW"],
"WWWE":["EEWE","EWEE"],
"EWEE":["WWWE","WWEW"],
"WEWW":["EEWE","EEEW"],
"EEEW":["WEWW","WWEW"],
"WWEW":["EWEE","EEEW","EWEW"],
"EWEW":["WWEW","WWWW"],
"WWWW":["EWEW"]
}


def bfs(G, node):
   visited = [] 
   visited.append(node)
   print(node, end = ' ')
   for key in G :
      for Gnode in G[key] :
         if Gnode not in visited :
            visited.append(Gnode)
            print(Gnode, end = ' ' )

                
bfs(G,'A')
print()
bfs(MCGW_G, "EEEE" )




