"""
This library provides a number of methods for manipulating a queue ADT.
"""

def enqueue(Q,n):
    """
    Input: Q, a queue and n, a new item
    Output: Return None
    Effect: n is put at the tail of Q
    """
    Q.append(n)
    return

def dequeue(Q):
    """
    Input: Q, a queue
    Output: Return the item at the head of Q
    Effect: The item at the head of Q is removed.
    """
    return Q.pop(0)

def peek(Q):
    """
    Input: Q, a queue
    Output: Return the item at the head of Q
    """
    return Q[0]

def size(Q):
    """
    Input: Q, a queue
    Output: Return the size of Q
    """
    return len(Q)

def isEmpty(Q):
    """
    Input: Q, a queue
    Output: Return True if Q is empty; False, otherwise
    """
    return not Q
