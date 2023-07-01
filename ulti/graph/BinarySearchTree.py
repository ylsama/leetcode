import json


class BinarySearchTree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.totalNode = 1
        self.countWayCache = None
        if self.left != None:
            self.totalNode += self.left.totalNode
        if self.right != None:
            self.totalNode += self.right.totalNode

    def addNode(self, value):
        if self.value > value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.addNode(value)

        if self.value < value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.addNode(value)
        
        self.totalNode += 1

    def toDict(self, nestedlevel = None):
        nextNestedLevel = nestedlevel
        if nestedlevel != None:
            nextNestedLevel = nestedlevel - 1
            if nextNestedLevel < 0:
                return "..."
            
        dictSeft = {}
        dictSeft["value"] = self.value
        if self.left != None:
            dictSeft["left"] = self.left.toDict(nextNestedLevel)
        if self.right != None:
            dictSeft["right"] = self.right.toDict(nextNestedLevel)
        return dictSeft

    def toString(self, nestedlevel = None, indent = 4):
        dictSeft = self.toDict(nestedlevel)
        stringSeft = json.dumps(dictSeft, indent = indent)
        return stringSeft

    def interator(self): 
        nodes = []
        nodes.append(self)
        if self.left != None:
            nodes.append(*self.left.interator())
        if self.right != None:
            nodes.append(*self.right.interator())
        return nodes