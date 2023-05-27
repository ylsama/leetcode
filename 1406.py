"""
# 1406. Stone Game III

    Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

    Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.

    The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.

    The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

    Assume Alice and Bob play optimally.

    Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.

 

## Example 1:

    Input: values = [1,2,3,7]
    Output: "Bob"
    Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.

## Example 2:

    Input: values = [1,2,3,-9]
    Output: "Alice"
    Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
    If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
    If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
    Remember that both play optimally so here Alice will choose the scenario that makes her win.
    
## Example 3:

    Input: values = [1,2,3,6]
    Output: "Tie"
    Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.
 

## Constraints:

    1 <= stoneValue.length <= 5 * 104
    -1000 <= stoneValue[i] <= 1000
"""

import random
from typing import List

class Solution:
    # Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an
    # associated value which is an integer given in the array stoneValue.

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = stoneValue.__len__()
        # player can take 1, 2, or 3 stones from the first remaining stones in the row.
        # when there is one or no remaining stone, the optimal play are the only way taking all the remain stone
        end_game_round = [{"remaining_stone": remaining_stone} for remaining_stone in range(2)]

        # Too long on caculating sum_stone_value using sum(stoneValue[n -i: n])
        # So we implement this
        # sum(stoneValue[n -i: n]) = sum_stone_value[n] -  sum_stone_value[n-i]
        sum_stone_value = [0 for i in range(n+1)]
        for i in range(1, n+1):
            sum_stone_value[i] = sum_stone_value[i-1] + stoneValue[i-1]

        # Loop from 1 to 3: Handling first case that only < 3 remaining stone left
        # Case stoneValue.__len__() = n < 3, set a min value to n
        for i in range(0, 2):
            # The score of each player is the sum of the values of the stones taken
            end_game_round[i] ["max_point"] = sum_stone_value[n] -  sum_stone_value[n-i]
            end_game_round[i]  = (end_game_round[i] ["remaining_stone"], end_game_round[i] ["max_point"]) 

        # Let use this infomation from the last round optimal play to find the first round optimal play
        optimal_play_point = [0 for remaining_stone in range(n+1)]
        for remaining_stone, max_point in end_game_round:
            optimal_play_point[remaining_stone] = max_point
        
        # Simulate each remaining_stone optimal_play
        # Where player try to get the max_point with current remaining_stone
        #   Knowing that:
        #       1. Next round is other player turn, they play optimaly, so they will get the optimal_play_point[remaining_stone]
        #       2. So, that mean we will lost that much point in the process till the end game round, we need to minimize this
        #       to find the best solution
        for remaining_stone in range(2, n+1):
            max_point = -100000*3
            for next_round_remaining_stone in range(max(0, remaining_stone-3),remaining_stone):
                if max_point <  sum_stone_value[n] -  sum_stone_value[n-remaining_stone] - optimal_play_point[next_round_remaining_stone]:
                    max_point = sum_stone_value[n] -  sum_stone_value[n-remaining_stone] - optimal_play_point[next_round_remaining_stone]
            optimal_play_point[remaining_stone] = max_point

        # Alice playing first, so there is all
        Alice_point = optimal_play_point[n]
        Bob_point = sum_stone_value[n] -  sum_stone_value[0] - Alice_point
        if Alice_point == Bob_point:
            game_result = "Tie"
        elif Alice_point > Bob_point:
            game_result = "Alice"
        else:
            game_result = "Bob"
        return game_result


if __name__=="__main__":
    a = Solution()
    result = a.stoneGameIII(stoneValue = [1,2,3,7])
    print(result, "\n Test 1 is ",result == "Bob")
    result = a.stoneGameIII(stoneValue = [1,2,3,-9])
    print(result, "\n Test 2 is ",result == "Alice")
    result = a.stoneGameIII(stoneValue = [1,2,3,6])
    print(result, "\n Test 3 is ",result == "Tie")
    result = a.stoneGameIII(stoneValue = [1,-1])
    print(result, "\n Test 4 is ",result == "Alice")
    result = a.stoneGameIII(stoneValue = [-1])
    print(result, "\n Test 5 is ",result == "Bob")
    result = a.stoneGameIII(stoneValue = [random.randint(-1000, 1000) for i in range(5 * (10**4))])
    print(result, "\n Test time limit is ","OK")


            
# 1406. Stone Game III

   
    # Alice and Bob take turns, with Alice starting first. On each player's turn, that 

    # . The score of each player is 0 initially.

    # The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

    # Assume Alice and Bob play optimally.

    # Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.