class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = strs[0]
        for eachWord in strs:
            if eachWord == "":
                return ""
            iterator = min(len(answer), len(eachWord))
            for i in range(iterator):
                if eachWord[i] != answer[i]:
                    answer = answer[0:i]
                    break
            else:
                answer = answer[0: iterator]
        return answer
