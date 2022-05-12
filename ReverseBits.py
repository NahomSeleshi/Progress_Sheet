class Solution:
    def reverseBits(self, n: int) -> int:
        stack = []
        while len(stack) < 32:
            stack.append(n%2)
            n = n//2
        number  = "".join(map(str, stack))
        return int(number, 2)
