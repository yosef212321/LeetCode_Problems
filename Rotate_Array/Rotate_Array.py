class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        leftpt = 0
        rightpt = len(nums) - 1
        while leftpt < rightpt:
            nums[leftpt], nums[rightpt] = nums[rightpt], nums[leftpt]
            leftpt += 1
            rightpt -= 1
        leftpt = 0
        rightpt = k - 1
        while leftpt < rightpt:
            nums[leftpt], nums[rightpt] = nums[rightpt], nums[leftpt]
            leftpt += 1
            rightpt -= 1
        leftpt = k
        rightpt = len(nums) - 1
        while leftpt < rightpt:
            nums[leftpt], nums[rightpt] = nums[rightpt], nums[leftpt]
            leftpt += 1
            rightpt -= 1

        
       
        
