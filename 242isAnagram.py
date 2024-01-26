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

# Testing
s = "anagram"
t = "nagaram"

s = "rat"
t = "car"

print(Solution().isAnagram(s, t))