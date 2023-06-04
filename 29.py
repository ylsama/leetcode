"""
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2**31, 2**31 − 1]. For this problem, if the quotient is strictly greater than 2**31 - 1, then return 2**31 - 1, and if the quotient is strictly less than -2**31, then return -2**31.
"""


# without using multiplication (*), division (//, /), and mod (%) operator
# we could still use:
#       add/sub:    +  - 
#       math:       log() abs()
#       bit:        xor ^    or |    and &    not ~
#       bit shift:  << >>
# First appoard: we can use only + or - operator, like this:
# function devide():
#       result = 0
#       sign = sign(result)
#       while unsign_dividend  >= 0:
#           unsign_dividend = unsign_dividend - unsign_divisor
#           result += 1
#       return result * sign
#
# Second appoard: we can fast up by using << shift bit operator (add a '0' on the right)
# the code implement:
#       1. Start with tmp_dividend = 0, result = 0
#
#       2. Store sign as seperate var, so the main handle only consider dividend and divisor as postive
#               sign = sign(result)
#               unsign_dividend = abs(dividend)
#               unsign_divisor = abs(divisor)
#               unsign_result = 0
#
#       3. While (tmp_dividend can be increase):
#               3.1. shift tmp_dividend left by 1 bit and
#               3.2. adding first bit of unsign_dividend to the right of tmp_dividend
#                   => tmp_dividend = tmp_dividend << 1 + unsign_dividend.pop(0)
#               3.3. shift unsign_result left by 1 bit
#                   unsign_result = unsign_result << 1
#               3.4. try to find tmp_dividend / unsign_divisor using first aproad devide()
#
#                   while tmp_dividend > unsign_divisor:
#                       tmp_dividend = tmp_dividend - divisor
#                       unsign_result += 1
#
#       4. Enforce 32 bit rule:
#               4.1. If unsign_result value >= 2**31-1 we need to set result back to 2**31 if the sign
#          variable is negitive or 2**32 -1 if sign is possitive.
#          - which here we could use bit shift to create binary with 31 number 1 instead of using ** operator
#          - we coud return result right here too
#
#                   if unsign_result > (1 << 31) - 1 and sign() is possitive:
#                       result = 1 << 31 - 1
#                       return result
#                   else if unsign_result > (1 << 31) and sign() is neigitive:
#                       result = 1 << 31
#                       return result
#
#       5. Add the sign back to result if 32 bit rule :
#               result = -unsign_result if sign is negitive
#
#          - If this is C++, we could run into trouble when dealling with unsign_result value = 2**31
#          as long long: can only represent [-2**31 .. 2**31 - 1] number range; 
#          - To work around this we need to set type unsign long long for unsign_result, which can
#          represent [0 .. 2**32] number range
#                   Step 4 is there handle unsign_result is in range [2**31 .. 2**32]
#          - But this mean in C++ need to be different than just set result = -unsign_result
#
#       6. Return final_result
from math import trunc
from random import randint


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            raise "Divide with 0"
        
        result = None
        result_value = 0
        unsign_dividend = abs(dividend)
        unsign_divisor = abs(divisor)
        sign_positive =  ((divisor >= 0) and (dividend >= 0)) or ((divisor < 0) and (dividend < 0))
        
        def popFirstBit(bin_number: str):
            remain_number = bin_number[1:]
            firstBit = int(bin_number[0])
            return remain_number, firstBit
        
        tmp_dividend = 0
        remain_dividend = bin(unsign_dividend)[2:]
        while len(remain_dividend) > 0:
            remain_dividend, firstBit = popFirstBit(remain_dividend)
            tmp_dividend = (tmp_dividend << 1) + firstBit
            result_value = result_value << 1

            while tmp_dividend >= unsign_divisor:
                tmp_dividend = tmp_dividend - unsign_divisor
                result_value += 1

        result = result_value
        if not sign_positive:
            result = -result_value
            if result < -(1 << 31):
                result = -(1 << 31)
        else:
            if result > (1 << 31) -1:
                result = (1 << 31) -1
        return result

def main():
    a = Solution()
    # Example 1:
    # Input:
    dividend = 10
    divisor = 3
    # Output: 
    result = 3
    print("Test 1 is", result == a.divide(dividend, divisor))
    # Example 2:
    # Input:
    dividend = 7
    divisor = -3
    # Output: 
    result = -2
    print("Test 2 is", result == a.divide(dividend, divisor))
    # Example 3:
    # Input:
    dividend = 1
    divisor = 1
    # Output: 
    result = 1
    print("Test 3 is", result == a.divide(dividend, divisor))
    # Example 4:
    # Input:
    dividend = -2147483648
    divisor = -1
    # Output: 
    result = 2147483647
    print("Test 4 is", result == a.divide(dividend, divisor))
    # Example 5:
    # Input:
    dividend = -2147483648
    divisor = 1
    # Output: 
    result = -2147483648
    print("Test 5 is", result == a.divide(dividend, divisor))
    # Random
    for test_number in range(1,10):
        dividend = randint(-2**31, 2**31-1)
        # divisor != 0
        divisor = randint(-2**31, 2**31-1)
        result = trunc(dividend/divisor)
        if result.bit_length() > 32:
            continue
        print(f"Test randome {test_number} is", result == a.divide(dividend, divisor))
    # Constraints:
    # -2**31 <= dividend, divisor <= 2**31 - 1
    dividend = 2**31-1
    # divisor != 0
    divisor = -3
    result = trunc(dividend/divisor)
    print("Test time limit is", result == a.divide(dividend, divisor))


if __name__ == "__main__":
    main()
