class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = nums
        for i in range(len(self.nums) - 1):
            self.prefix[i + 1] += nums[i]
    def sumRange(self, left: int, right: int) -> int:
        self.left = left
        self.right = right
        if self.left:
            return self.prefix[right] - self.prefix[left - 1]
        else:
            return self.prefix[right]
            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
