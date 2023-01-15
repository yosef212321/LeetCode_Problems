class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        leftpt = 0
        rightpt = len(people) - 1
        ans = 0
        while leftpt < rightpt:
            if people[leftpt] + people[rightpt] <= limit:
                ans += 1
                leftpt += 1
                rightpt -= 1
            else:
                ans += 1
                rightpt -= 1
        if rightpt == leftpt:
            ans += 1
        return ans
