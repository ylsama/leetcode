"""
A graph class

Simple way to do a dfs/bfs to search through all the node.
/
"""
from random import randint
from typing import Dict, List

class GraphNode:
    def __init__(self, ID):
        self.ID = ID
        self.connectedNode = []
    
    def addConnectedNode(self, node):
        self.connectedNode.append(node.ID)
        return self.connectedNode

    def isConnected(self, node):
        return node.ID in self.connectedNode

    def getID(self):
        return self.ID
    
    def getConnectedNode(self):
        return self.connectedNode
    
    def __hash__(self):
        return self.ID
    
class Graph:
    def __init__(self, nodeList: Dict(int, GraphNode) = {}, nodeAdjTable : dict = {}):
        self.nodeList = nodeList
        self.nodeAdjTable = nodeAdjTable

    def getNodeByID(self, nodeID: int):
        if nodeID in self.nodeList:
            return (self.nodeList[nodeID], True)
        return (None, False)

    def getTotalNodeInGraph(self):
        return len(self.nodeList.keys())
    
    def getNodeList(self):
        return self.nodeList

    def addNode(self, node: GraphNode):
        self.nodeList[node.getID()] = node


class Graph_DFS:
    def __init__(self, graph: Graph = None):
        self.graph = graph
        self.traceVisitedNode = {}
        for node in graph.getNodeList:
            self.traceVisitedNode[node] = False
    
    def getNotVisitedNode(self):
        result = -1
        isNotVisitedNodeFound = False
        
        for nodeID in self.nodeList:
            if self.traceDfs_VisitedNode[nodeID]:
                continue
            result = nodeID
            isNotVisitedNodeFound = True
            break
        return result, isNotVisitedNodeFound
        
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        result = 0
        
        # DFS
        self.traceDfs_VisitedNode = [False]*totalNode
        queue = []
        MAX_QUEUE_LOOP = totalNode
        self.cacheAdjNodeList = {}
          
        for index in range(MAX_QUEUE_LOOP):
            adjNode = []
            
            if len(queue) == 0:
                notVisitedNodeID, isFound = self.getNotVisitedNode()
                if isFound:
                    queue.append(notVisitedNodeID)
                    result = result + 1
                    self.traceDfs_VisitedNode[notVisitedNodeID] = True
                else:
                    break
                    
            currentVisitedNodeID = queue.pop(0)
            
            adjNodes = self.findAdjNode(currentVisitedNodeID)
            for nodeID in adjNodes:
                if self.traceDfs_VisitedNode[nodeID]:
                    continue
                queue.append(nodeID)
                self.traceDfs_VisitedNode[nodeID] = True
        return result



if __name__ == "__main__":
    main()