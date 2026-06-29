class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if len(t) > len(s):
            return ""
        mp = {}
        for c in t:
            mp[c] = mp.get(c, 0) + 1
        i = j = 0
        start_i = 0
        requiredCount = len(t)
        minWindowSize = float('inf')
        while j < n:
            ch = s[j]
            if ch in mp and mp[ch] > 0:
                requiredCount -= 1
            mp[ch] = mp.get(ch, 0) - 1
            while requiredCount == 0:
                currentWindowSize = (j-i+1)
                if currentWindowSize < minWindowSize:
                    minWindowSize = currentWindowSize
                    start_i = i
                startChar = s[i]
                mp[startChar] = mp.get(startChar, 0) + 1
                if startChar in mp and mp[startChar] > 0:
                    requiredCount += 1
                i += 1
            j += 1
        return "" if minWindowSize == float('inf') else s[start_i:start_i+minWindowSize]

                
