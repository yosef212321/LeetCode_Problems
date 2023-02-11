class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = deque(piles)
        tot = 0
        
        while piles:
            piles.pop()
            tot += piles.pop()
            piles.popleft()
        
        return tot
