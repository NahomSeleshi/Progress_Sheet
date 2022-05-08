class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lettersHash = {}
        lettersFromT = set()
        for i in range(len(s)):
            if s[i] in lettersHash:
                if lettersHash[s[i]] != t[i]:
                    return False
            else:
                if t[i] in lettersFromT:
                    return False
                lettersFromT.add(t[i])
                lettersHash[s[i]] = t[i]
        
        return True
