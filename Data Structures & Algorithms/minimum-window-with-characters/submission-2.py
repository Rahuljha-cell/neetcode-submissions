class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if len(t) > n:
            return ""
        mp = {}
        for c in t:
            mp[c] = mp.get(c, 0) + 1

        i = j = 0
        start_i = 0
        minWindowSize = float('inf')
        requiredCount = len(t)
        while j < n:
            ch = s[j]
            if ch in mp and mp[ch] > 0:
                requiredCount -= 1
            mp[ch] = mp.get(ch, 0) - 1
            while requiredCount == 0:
                currentWindowSize = j - i + 1
                if currentWindowSize < minWindowSize:
                    minWindowSize = currentWindowSize
                    start_i = i
                startCh = s[i]
                mp[startCh] = mp.get(startCh, 0) + 1
                if startCh in mp and mp[startCh] > 0:
                    requiredCount += 1
                i+=1
            j += 1
        return "" if minWindowSize == float('inf') else s[start_i:start_i+minWindowSize]
                    


