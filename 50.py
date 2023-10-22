"""
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

"""

import time

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
    
    def pow(self, x, n, modulo):
        if n == 0:
            return 1 % modulo
        if n == 1:
            return x % modulo
        half_pow = self.pow(x,n//2,modulo) % modulo
        return half_pow*half_pow*pow(x,n %2, modulo)


if __name__ == "__main__":
    a = Solution()
    t1 = time.time()
    first = a.pow(1359123,15650123,50500000) 
    t2 = time.time()
    print(f"Crafted pow function completed time = {t2-t1} \nresult = {first}")
    t1 = time.time()
    second = pow(1359123, -15)
    t2 = time.time()
    print(f"Native pow function completed time = {t2-t1} \nresult = {second}")
    print(first == second)

"""
Let be real and sane with your self, math is hard and you use computer to do math, even the python having a pow function to do eaxactly this
    - The problem do not provided max cap for result.
    - Floating point saving its
    - They use floating point which it self already being a hardware problem.

Here is some real case that you want a real pow function
    1. RSA Modular exponentiation
            RSA using big number, where they do alot of exponentiation operation in a Modular range
    This require some quick crafted pow function with O(log(n)) time:
        def pow(x, n, modulo):
            if n == 0:
                return 1 % modulo
            if n == 1:
                return x % modulo
            half_pow = pow(x,n//2) % modulo
            return half_pow*half_pow*pow(x,n %2)
"""