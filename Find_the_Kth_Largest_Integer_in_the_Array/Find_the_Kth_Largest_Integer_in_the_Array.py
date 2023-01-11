class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ans = []
        for x in nums:
            ans.append(int(x))
        ans.sort(reverse = True)
        return str(ans[k - 1])
