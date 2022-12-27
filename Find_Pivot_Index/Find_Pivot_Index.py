class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        total = sum(nums)
        for x, y in enumerate(nums):
            if leftSum == (total - nums[x] - leftSum):
                return x
            leftSum += nums[x]
        return -1
                

                   
            
            
         
            
               

            
        
        
            
