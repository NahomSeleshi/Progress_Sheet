class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        # bitwise operation of the number and number - 1 will
        # result 0 if the number is power of two else it returns
        # a number different from 0
        
        return False if n & (n-1) else True
