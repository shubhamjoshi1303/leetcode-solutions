class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set()
        res = 0 

        for x in word :
            if x in s:
                continue
            
            if x.isupper() and x.lower() in s :
                res+=1
            elif x.islower() and x.upper() in s:
                res+=1
            
            s.add(x)
        return res