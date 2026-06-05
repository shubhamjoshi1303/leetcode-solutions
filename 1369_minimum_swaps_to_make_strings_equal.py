class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1

        diff = {"x": 0 , "y" : 0}
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff[s1[i]] += 1
        
        if diff["x"]%2 != diff["y"] %2:
            return -1 
        count = diff["x"] // 2 + diff["y"] // 2
        if diff["x"] % 2 == 1:
            return count + 2
        return count