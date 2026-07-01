class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(t)
        if n > len(s):
            return ""
        mp = {}
        for c in t:
            mp[c] = mp.get(c, 0) + 1
        i = j = 0
        start_i = 0
        minWindowSize = float('inf')
        requiredCount = len(t)
        while j < len(s):
            ch = s[j]
            if ch in mp and mp[ch] > 0:
                requiredCount -= 1
            mp[ch] = mp.get(ch, 0) - 1
            while requiredCount == 0:
                currWindowSize = j-i+1
                if minWindowSize > currWindowSize:
                    minWindowSize = currWindowSize
                    start_i = i
                starCh = s[i]
                mp[starCh] = mp.get(starCh, 0) + 1
                if starCh in mp and mp[starCh] > 0:
                    requiredCount += 1
                i += 1
            j += 1
        return "" if minWindowSize == float('inf') else s[start_i:start_i+minWindowSize]
            

                



        