class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        freq = Counter(changed)
        changed.sort()
        if n % 2 != 0: return []
        
        ans = []
        for i, v in enumerate(changed):
            if freq[v] > 0:
                if v == 0 and freq[0] < 2: return []
                if v*2 not in freq or freq[v*2] == 0: return []
                freq[v] -= 1
                freq[v*2] -= 1
                ans.append(v)
        return ans
            
