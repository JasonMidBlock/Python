def genStatesSorted(order):
    """
    A function to generate a set of all possible states (E/W,E/W,E/W,E/W)
    Input: None
    Output: Return a tuple of all possible states (E/W,E/W,E/W,E/W) in two sorted orders:
            - Order = 0: alphabetical order
            - Order = 1: reverse alphabetical order
    """

    if order == 0:
        direction = ["E","W"]
    else:
        direction = ["W","E"]

    states = []
    for i in direction:
        for j in direction:
            for k in direction:
                for l in direction:
                    aState = i + j + k + l  # Concatenate the four locations into a string
                    states.append(aState)   # Add the newly created state to the set of states

    return tuple(states)
    
print("Alphabetic order:")
for state in genStatesSorted(0):
    print(state)

print("\nReverse alphabetic order:")
for state in genStatesSorted(1):
    print(state)

