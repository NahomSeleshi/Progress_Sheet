# Here, we will start from the end of the range and calulate the end AND with end - 1.
# After that, we will set the end to the result of the AND operation. This is 
# because, if we bitwise and two numbers, the result is always less than or equal to the
# smaller number. So, working with the values between end - 1 and the result of our 
# operation is not necessary. For example, if we bitwise and 12 and 11, the result is 8.
# So, ANDing 9 and 10 is not necessary after this because we know that it will always result
# 8 or less than it. So, this is the reason we move "right" to the result of the AND operation.

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while(right > left):
            right = right & right - 1
        return right
