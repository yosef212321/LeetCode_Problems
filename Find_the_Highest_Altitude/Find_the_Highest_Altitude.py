class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = [0]
        for i in range(len(gain)):
            ans.append(gain[i] + ans[i])
        return max(ans)
