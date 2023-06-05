"""
1232. Check If It Is a Straight Line
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""

from typing import List
from math import sqrt

class Solution:
    """
    Normalizing a vector involves converting it to a “unit vector” with a standard magnitude, usually 1
    This can be done by devide both (x,y) with vector length
    The result also contain revertNomalizedVector (-x, -y) as both are consider “unit vector” with a standard magnitude 1
    """
    def getNomalizedVector(self, vector):
        x,y = vector
        vectorLength = sqrt(x**2 + y**2)
        nomalizedVector = (x/vectorLength, y/vectorLength)
        revertNomalizedVector = (-x/vectorLength, -y/vectorLength)
        return [nomalizedVector, revertNomalizedVector]
    
    """
    This handle compare of two floating point variable, using a epsilon = 0.000000001 to detect if both are the same vector
    """
    def isSameVector(self, vector1, vector2):
        x1,y1 = vector1
        x2,y2 = vector2
        return (abs(x1 - x2) < 0.000000001 ) and (abs(y1 - y2) < 0.000000001 )
    
    """
    This set a basePoint, which hard code to be coordinates[0]
    Main handle:
        1. Caculate every vector from basePoint to another point in coordinates array
        2. Normalize caculated vector
        3. Compare vector if they are the same, if not, they isn't on the same line 
    """
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        result = True
        
        basePoint = coordinates[0]
        baseVector = None
        
        for point in coordinates[1:]:
            x1, y1 = tuple(basePoint)
            x2, y2 = tuple(point)
            vector = (x1 - x2, y1 - y2)
            nomalizedVector = self.getNomalizedVector(vector)
            if baseVector == None:
                baseVector = nomalizedVector
            
            if self.isSameVector(baseVector[0], nomalizedVector[0]) \
            or self.isSameVector(baseVector[1], nomalizedVector[0]):
                continue
                
            print(baseVector)
            print(nomalizedVector)
            result = False
            break
        return result
    
    
def test():
    a = Solution()
    # Example 1:
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    result = True
    
    print("Test 1 is", a.checkStraightLine(coordinates) == result)
    # Example 2:
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    result = True
    
    print("Test 2 is", a.checkStraightLine(coordinates) == result)
    
if __name__ == "__main__":
    test()