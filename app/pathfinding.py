# Takes a list of lists of nodes, as well as a list of nuggets.
# These nodes each contain an adjacency list of other nodes,
# as well as a weight.
# Also takes our current position (start).

import math

def Dijkstra(board, nuggets, start):
    # When Dijkstra's starts, the distance to every node is infinite,
    # and there is no path to any node.
    for list in board:
        for node in list:
            node.dist = math.inf
            node.prev = None

    # The distance to our starting point is zero.
    start.dist = 0

    Queue = []
    for node in start.adj:
        node.prev = start
        node.dist = start.dist + node.weight
        Queue.append(node)

    while len(Queue) > 0:
        Queue.sort(key=lambda x: x.dist)
        current = Queue.pop(0)
        for node in current.adj:
            if node.prev == None:
                node.prev = current
                node.dist = current.dist + node.weight
                Queue.append(node)
            else:
                if node.dist > current.dist + node.weight:
                    node.dist = current.dist + node.weight
                    node.prev = current

    nuggets.sort(key=lambda x: x.dist)
    if nuggets[0].dist == math.inf:
        return "down"
    nextNugget = nuggets[0]
    nextNode = nextNugget
    path = []
    while nextNode is not start:
        path.insert(0, nextNode)
        nextNode = nextNode.prev
    nextNode = path.pop(0)
    if nextNode.x > start.x:
        return "right"
    elif nextNode.x < start.x:
        return "left"
    elif nextNode.y > start.y:
        return "down"
    else:
        return "up"
