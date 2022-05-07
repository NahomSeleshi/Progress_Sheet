class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        lettersHash = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'],
                       5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'],
                       8:['t','u','v'], 9:['w','x','y','z']}
        
        def dfs(string, index):
            if index >= len(digits):
                if string == "":
                    return 
                answer.append(string)
                return
            
            temp = lettersHash[int(digits[index])]
            for i in temp:
                currentString = string
                dfs(currentString + i, index + 1)
        
        dfs("", 0)
        return answer
