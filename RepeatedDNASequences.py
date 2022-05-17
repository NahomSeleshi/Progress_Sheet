class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        answer = set()
        allSequences = set()
        for i in range(len(s)-9):
            temp = s[i:i+10]
            if temp in allSequences:
                answer.add(temp)
            else:
                allSequences.add(temp)
        return answer
