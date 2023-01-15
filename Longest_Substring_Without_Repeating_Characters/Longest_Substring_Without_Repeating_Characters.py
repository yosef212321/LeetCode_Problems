class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftpt = 0
        charset = set()
        ans = 0
        for rightpt in range(len(s)):
            while s[rightpt] in charset:
                charset.remove(s[leftpt])
                leftpt += 1
            charset.add(s[rightpt])
            ans = max(ans, rightpt - leftpt + 1)
        return ans
