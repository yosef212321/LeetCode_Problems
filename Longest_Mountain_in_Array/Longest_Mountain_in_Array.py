class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ans = 0
        for i in range(1,len(arr) - 1):
            count = 1
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                j = i
                while j > 0 and arr[j] > arr[j - 1]:
                    j -= 1
                    count += 1
                while i < len(arr) -1 and arr[i] > arr[i + 1]:
                    i += 1
                    count += 1
                ans = max(count, ans)
            count = 0
        return ans


            

        
