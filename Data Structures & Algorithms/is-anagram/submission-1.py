class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = list(s)
        char_t = list(t)
        if len(s) != len(t):
            return False
        list.sort(char_s)
        list.sort(char_t)
        for i in range(0, len(s)):
            if char_s[i] != char_t[i]:
                return False
        return True
