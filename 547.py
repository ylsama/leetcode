"""
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces
"""

"""
Solution: This just a graph problem, where you try to seperate graph into distinc group of Node and there there are no route from one group to another

Simple way is to use a dfs/bfs to search through all the node. Total time we have to manualy call dfs/bfs until all node is visited is the result
"""
from random import randint
from typing import List

class Solution:
    def findAdjNode(self, currentVisitedNode):
        adjNodes = []
        
        if currentVisitedNode in self.cacheAdjNodeList:
            adjNodes = self.cacheAdjNodeList[currentVisitedNode]
            return adjNodes
            
        for nodeID in self.nodeList:
            if self.nodeAdjTable[currentVisitedNode][nodeID]:
                adjNodes.append(nodeID)
                
        self.cacheAdjNodeList[currentVisitedNode] = adjNodes
        
        return adjNodes
    
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
        totalNode = len(isConnected)
        self.nodeList = [nodeID for nodeID in range(totalNode)]
        self.nodeAdjTable = isConnected
        
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

    
    
def main():
    a = Solution()
    # Example 1:
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    result = 2
    print('Test 1 is',a.findCircleNum(isConnected), a.findCircleNum(isConnected) == result)
    
    # Example 2:
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    result = 3
    print('Test 2 is',a.findCircleNum(isConnected), a.findCircleNum(isConnected) == result)
    
    # Constraints limit test:
    # 1 <= n <= 200
    isConnected = [[randint(0,1) for j in range(200)] for i in range(200)]
    print('Test time limit is OK')



if __name__ == "__main__":
    main()