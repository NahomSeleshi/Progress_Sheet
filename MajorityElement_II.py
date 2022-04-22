class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numFrequency = {}
        answer = []
        for i in nums:
            if i in numFrequency:
                numFrequency[i] += 1
            else:
                numFrequency[i] = 1
        majorityNumber = len(nums)//3
        nums = set(nums)
        for i in nums:
            if numFrequency[i] > majorityNumber:
                answer.append(i)
        return answer
        
        
