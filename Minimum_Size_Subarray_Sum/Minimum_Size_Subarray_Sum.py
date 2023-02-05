class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        leftpt = 0
        sum1 = 0
        for rightpt in range(len(nums)):
            sum1 += nums[rightpt]
            while sum1 >= target:
                ans = min(rightpt - leftpt + 1, ans)
                sum1 -= nums[leftpt]
                leftpt += 1
        if ans == float("inf"):
            return 0
        else:
            return ans
