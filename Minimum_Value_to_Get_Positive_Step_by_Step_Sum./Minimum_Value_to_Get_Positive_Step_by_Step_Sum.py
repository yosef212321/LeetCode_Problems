class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixSum = 0
        startValue = 1
        for x in nums:
            prefixSum += x
            startValue = max(startValue, 1 - prefixSum)
        return startValue
