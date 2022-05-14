class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numberFrequency = Counter(nums)
        
        for eachKey in numberFrequency:
            if numberFrequency[eachKey] == 1:
                return eachKey
