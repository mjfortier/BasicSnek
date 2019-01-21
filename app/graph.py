from enum import Enum
import math

class NodeType(Enum):
    EMPTY = 0
    SNAKE = 1
    NUGGET = 2
    HEAD = 3

class Node:
    def __init__(self, x, y):
        self.adj = []
        self.weight = 10
        self.dist = math.inf
        self.prev = None
        self.type = None
        self.x = x
        self.y = y
    
    #Adjancency list always goes N, E, S, W
    def setAdjList(self, board):
        x = self.x
        y = self.y
        
        if y-1 > -1 and board.getNode(x,y-1) != NodeType.SNAKE:
            self.adj.append(board.getNode(x,y-1))

        if x+1 < board.getWidth() and board.getNode(x+1, y) != NodeType.SNAKE:
            self.adj.append(board.getNode(x+1, y))

        if y+1 < board.getHeight() and board.getNode(x, y+1) != NodeType.SNAKE:
            self.adj.append(board.getNode(x, y+1))

        if x-1 > -1 and board.getNode(x-1, y) != NodeType.SNAKE:
            self.adj.append(board.getNode(x-1, y))


class Board:
    def __init__(self, data):
        self.height = data["board"]["height"]
        self.width = data["board"]["width"]
        self.board = []
        self.nuggets = []
        self.head = None

        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(Node(x,y))
            self.board.append(row)
        
        self.updateBoard(data)

    def getNode(self, x, y):
        return self.board[y][x]
    
    def updateBoard(self, data):
        for row in self.board:
            for node in row:
                node.type = NodeType.EMPTY

        self.nuggets = []
        for nugget in data["board"]["food"]:
            self.getNode(nugget["x"], nugget["y"]).type = NodeType.NUGGET
            self.nuggets.append(self.getNode(nugget["x"], nugget["y"]))

        for snake in data["board"]["snakes"]:
            for body in snake["body"]:
                self.getNode(body["x"], body["y"]).type = NodeType.SNAKE
        
        head = data["you"]["body"][0]
        self.getNode(head["x"], head["y"]).type = NodeType.HEAD
        self.head = self.getNode(head["x"], head["y"])

        for y, row in enumerate(self.board):
            for x, node in enumerate(row):
                if node.type is None:
                    node.type == NodeType.EMPTY
                if node.type != NodeType.SNAKE:
                    node.setAdjList(self)


    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def printBoard(self):
        result = ""
        for  row in self.board:
            for node in row:
                result = result + " " + str(node.type)
            result = result + "\n"
        print(result)
