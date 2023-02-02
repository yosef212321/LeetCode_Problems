class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        sum2 = 0
        for i in range(len(nums)):
            if sum2 == sum1 - nums[i]:
                return i
            sum1 -= nums[i]
            sum2 += nums[i]
        return -1
