# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alpha = {}
        # Collect count 
        for c in s:
            if c not in alpha:
                alpha[c] = 1
                continue
            alpha[c] += 1
        # isAnagram
        print(alpha)
        for c in t:
            if c in alpha and alpha[c] > 0:
                alpha[c] -= 1
                continue
            return False
        return True
    
    def isAnagramv2(self, s: str, t: str) -> bool:
        # Comparison method
        if len(s) != len(t):
            return False
        sCount = {}
        tCount = {}
        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0) 
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        return sCount == tCount

# Testing
s = "anagram"
t = "nagaram"

s = "rat"
t = "car"

print(Solution().isAnagram(s, t))

print(Solution().isAnagramv2(s, t))