#Using a Counter class to count the frequency
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numFrequency = Counter(nums)
        for eachKey in numFrequency:
            if numFrequency[eachKey] >= 2:
                return eachKey


#Using binary Search
#Here, we are using the index of the array not the values in the array
#See the Pigeonhole Principle
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)-1
        while (left < right):
            mid = left + (right - left)//2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        
        return left
