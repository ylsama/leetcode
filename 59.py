from typing import List


class Solution:
    def checkValidate(self,x,y):
        if x >= self.n:
            return False
        if y >= self.n:
            return False
        if x < 0:
            return False
        if y < 0:
            return False
        if self.result[x][y]  >= 0:
            return False
        return True
    
    def turn(self, movingVector):
        if movingVector['x'] != 0:
            movingVector['y'] = 0 - movingVector['x']
            movingVector['x'] = 0
        elif movingVector['y'] != 0:
            movingVector['x'] = movingVector['y']
            movingVector['y'] = 0
        return movingVector
    
    def generateMatrix(self, n: int) -> List[List[int]]:
        self.result = [[-1 for i in range(n)] for i in range(n)]
        self.n = n
        x, y = 0, 0
        movingVector = {}
        movingVector["x"] = 0
        movingVector["y"] = 1
        value = 1
        stuck = False 
        while not stuck:
            self.result[x][y] = value
            value += 1
            x_next, y_next = x + movingVector["x"], y + movingVector["y"]
            if self.checkValidate(x_next, y_next):
                x,y = x_next, y_next
                continue

            newVector = movingVector.copy()
            for i in range(4):
                newVector = self.turn(newVector)
                x_next, y_next =  x + newVector["x"], y + newVector["y"]
                print("stuck", "try", x,y, newVector, x_next, y_next)
                if self.checkValidate(x_next, y_next):
                    x,y = x_next, y_next
                    movingVector = newVector
                    break
            
            if not self.checkValidate(x_next, y_next):
                stuck = True

            
            for i in self.result:
                print(i)
        return self.result
    
    def generateMatrix_2(self, n: int) -> List[List[int]]:
        # dx, dy is movingVector to caculating new position from (x, y); which is (x+dx, y+dy)
        # we can go 4 direction: 
        #   Left: (dx, dy) = (0, 1);
        #   Right: (dx, dy) = (0, -1);
        #   Up: (dx, dy) = (-1, 0);
        #   Down: (dx, dy) = (1, 0);
        # When hitting maxtrix's border or already steped maxtrix's tile, we alway turn right, so we need to just simmulate turn right function for each movingVector: Which mean Left -> Up; Up -> Right; Right -> Down; Down -> Left
        result = [[-1 for i in range(n)] for i in range(n)]
        x, y, dx, dy = 0, 0, 0 , 1
        value = 1
        stuck = False 
        for value in range(1,n*n+1):
            result[x][y] = value
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and  0 <= ny < n:
                if result[nx][ny] == -1:
                    x, y = nx, ny
                    continue
            # If above code not execute, meanning we hitting maxtrix's border or already steped maxtrix's tile
            # Turning right
            if dx == 0:
                dx, dy = dy, 0
            else:
                dx, dy = 0, 0 - dx
            nx, ny = x + dx, y + dy
            x, y = nx, ny
        return result

if __name__=="__main__":
    a = Solution()
    result = a.generateMatrix_2(5)
    for i in result:
        print(i)