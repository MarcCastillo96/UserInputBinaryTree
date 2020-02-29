class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        if data is None:
            self.data = inputNode()
        else:
            self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


def inputNode():
    user_inputNode = input("Enter Node: ")
    return user_inputNode


qtyOfNodes = input()
node = Node(None)
qtyOfNodes = int(qtyOfNodes) - 1
for x in range(qtyOfNodes):
    node.insert(inputNode())

node.printTree()
