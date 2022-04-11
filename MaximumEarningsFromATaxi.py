# This is a bottom-up DP implementation of the "Maximum Earnings From A Taxi" problem
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        n = len(rides)
        dp = [0]*(n+1)
        dp[n] = 0
        
        # this array holds only the start values of all the passangrs
        start = [num[0] for num in rides]
        
        for i in range(n-1, -1, -1):
            notpick = dp[i+1]
            gain = rides[i][1]-rides[i][0]+rides[i][2]
            
            # this bisect function is works as a binary search to find the next
            # possible index that I can pick ("bisect_left" gives the left possibl index
            next = bisect.bisect_left(start, rides[i][1])
            pick = gain + dp[next]
            
            dp[i] = max(pick, notpick)
            
        return dp[0]
            
