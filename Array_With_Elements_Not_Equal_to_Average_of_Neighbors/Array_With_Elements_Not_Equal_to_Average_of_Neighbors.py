class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums) - 1):
            prev, curr, nxt = nums[i - 1], nums[i], nums[i + 1]
            if prev < curr < nxt or prev > curr > nxt:
                nums[i], nums[i + 1] = nums[i + 1],nums[i]
        return nums
