class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict1 = {0: 1}
        ans = 0
        sum1 = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            if sum1 - k in dict1:
                ans += dict1[sum1 - k]
            if sum1 in dict1:
                dict1[sum1] += 1
            else:
                dict1[sum1] = 1
        return ans
        
