class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted([int(t[:2]) * 60 + int(t[3:]) for t in timePoints])
        minutes += [m + 24*60 for m in minutes]
        
        minimumDifference = float('inf')
        
        for i in range(1,len(minutes)):
            minimumDifference = min(minimumDifference, minutes[i]-minutes[i-1])
            
        return minimumDifference
