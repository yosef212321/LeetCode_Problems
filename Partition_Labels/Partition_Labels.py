class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {}
        ans = []
        count, end = 0, 0
        for i in range(len(s)):
            lastindex[s[i]] = i
        for i in range(len(s)):
            count += 1
            end = max(end, lastindex[s[i]])
            if i == end:
                ans.append(count)
                count = 0
        return ans
