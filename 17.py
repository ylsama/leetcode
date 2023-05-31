# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


# This is fairly simple question, just need some basic data structure to store provided/result data
# Here I using:
#       Python dictionary and string to map each number with each character; 
#       an array to store result data
# Main handling is loop through all inputed digit, 
#       With each step, add all of corresponds character to result table
#       Update the new result table and repeat
#
# There is a specical case when result blank, which i handling by append directly num_dict[digit]
#       to result table or above loop alway return [] blank
# From the second digit, we will follow to add each character to the last step result table

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        for digit in digits:
            tmp = []
            if len(result) > 0:
                for j in result:
                    for c in num_dict[digit]:
                        tmp.append(j+c)
            else:
                for c in num_dict[digit]:
                    tmp.append(c)
            result = tmp
        return result

if __name__ == "__main__":
    a = Solution()
    # Example 1:
    #     Input: digits = "23"
    #     Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    Output = a.letterCombinations(digits = "23")
    print("Test 1 is ", Output, set(Output) == set(["ad","ae","af","bd","be","bf","cd","ce","cf"]))
    # Example 2:
    #     Input: digits = ""
    #     Output: []
    Output = a.letterCombinations(digits = "")
    print("Test 2 is ", Output, set(Output) == set([]))
    # Example 3:
    #     Input: digits = "2"
    #     Output: ["a","b","c"]
    Output = a.letterCombinations(digits = "2")
    print("Test 3 is ", Output, set(Output) == set(["a","b","c"]))
    # Constraints:
    #     0 <= digits.length <= 4
    #     digits[i] is a digit in the range ['2', '9'].
    Output = a.letterCombinations(digits = "23456")
    print("Test time limit is OK")