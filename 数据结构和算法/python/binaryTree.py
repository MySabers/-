# 二叉排序树的实现
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.leftNode = None
        self.rightNode = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def getLeftNode(self):
        return self.leftNode

    def getRightNode(self):
        return self.rightNode

    def setLeftNode(self, node):
        self.leftNode = node

    def setRightNode(self, node):
        self.rightNode = node


class BinarySearchTree(object):
    def __init__(self):
        self.tree = None
    
    def insert(self, data):
        if not self.tree:
            self.tree = Node(data)
            return
        currentNode = self.tree
        while True:
            if currentNode.getData() >= data:
                if currentNode.getRightNode():
                    currentNode = currentNode.getRightNode()
                    continue
                else:
                    currentNode.setRightNode(Node(data))
                    break
            else:
                if currentNode.getLeftNode()
                    currentNode = currentNode.getLeftNode()
                    continue
                else:
                    currentNode.setLeftNode(Node(data))
                    break

    def select(self, data):
        currentNode = self.tree
        while currentNode != None:
            if currentNode.getData() > data:
                currentNode = currentNode.getRightNode()
            elif currentNode.getData() < data:
                currentNode = currentNode.getLeftNode()
            else:
                return currentNode
        return currentNode

    def delete(self, data):
        currentNode = self.tree
        currentNodeParent = None
        while currentNode != None:
            if currentNode.getData() > data:
                currentNode = currentNode.getRightNode()
            elif currentNode.getData() < data:
                currentNode = currentNode.getLeftNode()
            else:
                return currentNode
        return currentNode